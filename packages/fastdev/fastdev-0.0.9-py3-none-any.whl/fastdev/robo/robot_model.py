from __future__ import annotations

import torch
from torch import Tensor

from fastdev.robo.kinematics_config import COMPACT_JOINT_SPEC_SIZE, JointType, KinematicsConfig
from fastdev.utils.tui import console
from fastdev.xform.transforms import expand_tf_mat

# fos.environ["TORCH_CUDA_ARCH_LIST"] = current_cuda_arch()

# name = "fastdev_kinematics"
# build_dir = _get_build_directory(name, verbose=False)
# extra_include_paths: list[str] = [FDEV_CSRC_ROOT]
# extra_cflags = ["-O3", "-DWITH_CUDA"]
# extra_cuda_cflags = ["-O3", "-DWITH_CUDA"]

# C: Any = None

# sources = []
# for ext in ["cpp", "cu"]:
#     sources.extend(glob.glob(os.path.join(FDEV_CSRC_ROOT, "kinematics", f"**/*.{ext}"), recursive=True))


# # if failed, try with JIT compilation
# if cuda_toolkit_available():
#     if os.listdir(build_dir) != []:
#         # If the build exists, we assume the extension has been built
#         # and we can load it.
#         with Timer("Loading extension"):
#             C = load(
#                 name=name,
#                 sources=sources,
#                 extra_cflags=extra_cflags,
#                 extra_cuda_cflags=extra_cuda_cflags,
#                 extra_include_paths=extra_include_paths,
#             )
#     else:
#         # Build from scratch. Remove the build directory just to be safe: pytorch jit might stuck
#         # if the build directory exists.
#         shutil.rmtree(build_dir, ignore_errors=True)
#         with Timer("Building extension"), console.status(
#             "[bold yellow]Building extension (This may take a few minutes the first time)",
#             spinner="bouncingBall",
#         ):
#             C = load(
#                 name=name,
#                 sources=sources,
#                 extra_cflags=extra_cflags,
#                 extra_cuda_cflags=extra_cuda_cflags,
#                 extra_include_paths=extra_include_paths,
#             )
# else:
#     console.print("[yellow]No CUDA toolkit found. NeuralTeleop will be disabled.[/yellow]")


def _build_joint_transform(joint_type: JointType, joint_axis: Tensor, joint_value: Tensor | None = None) -> Tensor:
    if joint_type == JointType.REVOLUTE:
        if joint_value is None:
            raise ValueError("Joint value must be provided for revolute joint.")
        c = torch.cos(joint_value)
        s = torch.sin(joint_value)
        t = 1 - c
        x, y, z = joint_axis
        rot_mat = torch.stack(
            [
                t * x * x + c,
                t * x * y - s * z,
                t * x * z + s * y,
                t * x * y + s * z,
                t * y * y + c,
                t * y * z - s * x,
                t * x * z - s * y,
                t * y * z + s * x,
                t * z * z + c,
            ],
            dim=-1,
        ).reshape(-1, 3, 3)
        tf_mat = torch.eye(4, device=rot_mat.device, dtype=rot_mat.dtype).repeat(rot_mat.shape[:-2] + (1, 1))
        tf_mat[..., :3, :3] = rot_mat
        return tf_mat
    elif joint_type == JointType.PRISMATIC:
        if joint_value is None:
            raise ValueError("Joint value must be provided for revolute joint.")
        x, y, z = joint_axis
        tl = torch.stack([x * joint_value, y * joint_value, z * joint_value], dim=-1).reshape(-1, 3)
        tf_mat = torch.eye(4, device=tl.device, dtype=tl.dtype).repeat(tl.shape[:-1] + (1, 1))
        tf_mat[..., :3, -1] = tl
        return tf_mat
    elif joint_type == JointType.FIXED:
        return torch.eye(4, dtype=torch.float32, device=joint_axis.device)
    else:
        raise NotImplementedError(f"Joint type {joint_type} is not supported.")


def torch_kinematics(kin_config: Tensor, joint_values: Tensor, root_poses: Tensor) -> Tensor:
    num_unique_links = int(kin_config[0].item())
    num_chains = int(kin_config[1].item())
    if num_chains > 1:
        console.print(
            "[bold red]Warning:[/bold red] There is no acceleration for parallel chains in pytorch forward kinematics,"
            " please set `parallel_chains` to `False`, or use cuda extension."
        )
    chain_lengths = [int(length) for length in kin_config[2 : num_chains + 2].tolist()]
    joint_spec_begin = 2 + num_chains

    joint_poses: list[Tensor] = []
    for chain_idx in range(num_chains):
        chain_joint_poses: list[Tensor] = []
        for joint_idx in range(chain_lengths[chain_idx]):
            glb_joint_idx = sum(chain_lengths[:chain_idx]) + joint_idx
            joint_spec = kin_config[
                joint_spec_begin + glb_joint_idx * COMPACT_JOINT_SPEC_SIZE : joint_spec_begin
                + (glb_joint_idx + 1) * COMPACT_JOINT_SPEC_SIZE
            ]
            joint_type = JointType(int(joint_spec[0].item()))
            active_joint_idx = int(joint_spec[1].item())
            parent_link_idx = int(joint_spec[2].item())
            link_idx_in_result = int(joint_spec[3].item())
            if joint_type == JointType.NONE:
                global_joint_tf = root_poses
            else:
                joint_origin = expand_tf_mat(joint_spec[4:16].reshape(3, 4))
                joint_axis = joint_spec[16:19]
                parent_joint_tf = chain_joint_poses[parent_link_idx]
                if active_joint_idx >= 0:
                    local_joint_tf = _build_joint_transform(joint_type, joint_axis, joint_values[:, active_joint_idx])
                else:
                    local_joint_tf = _build_joint_transform(joint_type, joint_axis)
                global_joint_tf = torch.matmul(torch.matmul(parent_joint_tf, joint_origin), local_joint_tf)

            chain_joint_poses.append(global_joint_tf)
            if link_idx_in_result != -1:
                joint_poses.append(global_joint_tf)
    if len(joint_poses) != num_unique_links:
        raise ValueError(
            f"Number of unique links {num_unique_links} does not match the number of joint poses {len(joint_poses)}."
        )
    return torch.stack(joint_poses, dim=1)  # [batch, num_links, 4, 4]


# class Kinematics(Function):
#     @staticmethod
#     def forward(
#         ctx,
#         kin_config_tensor: Tensor,
#         joint_values: Tensor,
#         root_poses: Tensor,
#     ):
#         return C.kinematics_forward(kin_config_tensor, joint_values, root_poses)

#     @staticmethod
#     def backward(ctx, grad_output):
#         pass


class RobotModel:
    """Robot model.

    Args:
        urdf_path (str): Path to the URDF file.
        device (torch.device | str | int, optional): Device. Defaults to "cpu".

    Examples:
        >>> robot_model = RobotModel("assets/panda.urdf", "cpu")
        >>> robot_model.num_dofs
        9
        >>> link_poses = robot_model.forward_kinematics(torch.zeros(1, 9))
        >>> torch.allclose(link_poses[0, -1, :3, 3], torch.tensor([0.088, 0, 0.868]), atol=1e-3)
        True
    """

    def __init__(self, urdf_path: str, device: torch.device | str | int = "cpu") -> None:
        self._kin_config = KinematicsConfig.from_urdf(urdf_path, device=device)
        self._device = torch.device(device)

    @property
    def num_dofs(self) -> int:
        return self._kin_config.num_dofs

    @property
    def active_joint_names(self) -> list[str]:
        return self._kin_config.active_joint_names

    @property
    def link_names(self) -> list[str]:
        return self._kin_config.link_order_in_compact_tensor

    @property
    def joint_limits(self) -> Tensor:
        return self._kin_config.joint_limits

    def forward_kinematics(self, joint_values: Tensor, root_poses: Tensor | None = None) -> Tensor:
        if root_poses is None:
            root_poses = torch.eye(4, device=joint_values.device).unsqueeze(0).expand(joint_values.shape[0], 4, 4)
        return torch_kinematics(self._kin_config.compact_tensor, joint_values, root_poses)


__all__ = ["RobotModel"]
