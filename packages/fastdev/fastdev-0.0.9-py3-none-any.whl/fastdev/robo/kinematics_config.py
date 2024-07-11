import os
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum

import numpy as np
import torch
import trimesh
import yourdfpy
from torch import Tensor

NONE_JOINT_NAME = "__none__"
COMPACT_JOINT_SPEC_SIZE = 19


class Geometry(ABC):
    @abstractmethod
    def get_trimesh(self) -> trimesh.Trimesh: ...


@dataclass
class Box(Geometry):
    size: list[float]

    def get_trimesh(self) -> trimesh.Trimesh:
        return trimesh.creation.box(self.size)


@dataclass
class Cylinder(Geometry):
    radius: float
    length: float

    def get_trimesh(self) -> trimesh.Trimesh:
        return trimesh.creation.cylinder(radius=self.radius, height=self.length)


@dataclass
class Capsule(Geometry):
    radius: float
    length: float

    def get_trimesh(self) -> trimesh.Trimesh:
        return trimesh.creation.capsule(radius=self.radius, height=self.length)


@dataclass
class Sphere(Geometry):
    radius: float

    def get_trimesh(self) -> trimesh.Trimesh:
        return trimesh.creation.icosphere(subdivisions=3, radius=self.radius)


@dataclass
class Mesh(Geometry):
    scale: list[float]

    filename: str | None = None
    vertices: np.ndarray | None = None
    faces: np.ndarray | None = None

    def get_trimesh(self) -> trimesh.Trimesh:
        if self.vertices is None or self.faces is None:
            assert self.filename is not None, "Either filename or vertices and faces must be provided"
            mesh: trimesh.Trimesh = trimesh.load_mesh(self.filename)  # type: ignore
            self.vertices, self.faces = mesh.vertices, mesh.faces
        return trimesh.Trimesh(self.vertices * np.asarray(self.scale), self.faces)


@dataclass
class Material:
    name: str | None = None
    color: np.ndarray | None = None
    texture: str | None = None


@dataclass
class Visual:
    origin: np.ndarray
    geometry: Geometry
    name: str | None = None
    material: Material | None = None

    def get_trimesh(self) -> trimesh.Trimesh:
        mesh = self.geometry.get_trimesh()
        return mesh.apply_transform(self.origin)


@dataclass
class Collision:
    origin: np.ndarray
    geometry: Geometry
    name: str | None = None

    def get_trimesh(self) -> trimesh.Trimesh:
        mesh = self.geometry.get_trimesh()
        return mesh.apply_transform(self.origin)


class JointType(Enum):
    NONE = -1  # used for base link, which has no parent joint
    FIXED = 0
    PRISMATIC = 1
    REVOLUTE = 2  # aka. rotational


@dataclass(frozen=True)
class Joint:
    name: str
    type: JointType
    origin: Tensor
    axis: Tensor
    limit: Tensor | None

    parent_link_name: str
    child_link_name: str


@dataclass(frozen=True)
class Link:
    name: str
    visuals: list[Visual] = field(default_factory=list)
    collisions: list[Collision] = field(default_factory=list)

    parent_joint_name: str = field(init=False)

    def set_parent_joint_name(self, parent_joint_name: str):
        object.__setattr__(self, "parent_joint_name", parent_joint_name)


def _str_to_joint_type(joint_type_str: str) -> JointType:
    if joint_type_str == "fixed":
        return JointType.FIXED
    elif joint_type_str == "prismatic":
        return JointType.PRISMATIC
    elif joint_type_str == "revolute":
        return JointType.REVOLUTE
    else:
        raise ValueError(f"Unknown joint type: {joint_type_str}")


def _build_joint_from_urdf(joint_spec: yourdfpy.urdf.Joint) -> Joint:
    joint_type = _str_to_joint_type(joint_spec.type)
    if joint_spec.limit is not None and joint_spec.limit.lower is not None and joint_spec.limit.upper is not None:
        limit = torch.tensor([joint_spec.limit.lower, joint_spec.limit.upper], dtype=torch.float32)
    else:
        limit = None
    return Joint(
        name=joint_spec.name,
        type=joint_type,
        origin=torch.from_numpy(joint_spec.origin).float(),
        axis=torch.from_numpy(joint_spec.axis).float(),
        limit=limit,
        parent_link_name=joint_spec.parent,
        child_link_name=joint_spec.child,
    )


def _build_geometry_from_urdf(urdf_geometry: yourdfpy.urdf.Geometry, mesh_dir: str) -> Geometry:
    if urdf_geometry.box is not None:
        return Box(size=urdf_geometry.box.size.tolist())
    elif urdf_geometry.cylinder is not None:
        return Cylinder(radius=urdf_geometry.cylinder.radius, length=urdf_geometry.cylinder.length)
    elif urdf_geometry.sphere is not None:
        return Sphere(radius=urdf_geometry.sphere.radius)
    elif urdf_geometry.mesh is not None:
        scale_spec = urdf_geometry.mesh.scale
        if isinstance(scale_spec, float):
            scale: list[float] = [scale_spec, scale_spec, scale_spec]
        elif isinstance(scale_spec, np.ndarray):
            scale = scale_spec.tolist()
        elif scale_spec is None:
            scale = [1.0, 1.0, 1.0]
        else:
            raise ValueError(f"Unknown scale type: {scale_spec}")
        mesh_path = os.path.join(mesh_dir, urdf_geometry.mesh.filename)
        return Mesh(filename=mesh_path, scale=scale)
    else:
        raise ValueError(f"Unknown geometry type: {urdf_geometry}")


def _build_material_from_urdf(urdf_material: yourdfpy.urdf.Material) -> Material:
    return Material(
        name=urdf_material.name,
        color=urdf_material.color.rgba if urdf_material.color is not None else None,
        texture=urdf_material.texture.filename if urdf_material.texture is not None else None,
    )


def _build_link_from_urdf(link_spec: yourdfpy.urdf.Link, mesh_dir: str) -> Link:
    link = Link(name=link_spec.name)
    for visual_spec in link_spec.visuals:
        assert visual_spec.geometry is not None, f"Visual {visual_spec.name} has no geometry"
        if visual_spec.origin is None:
            origin = np.eye(4, dtype=np.float32)
        else:
            origin = visual_spec.origin
        visual = Visual(
            origin=origin,
            geometry=_build_geometry_from_urdf(visual_spec.geometry, mesh_dir=mesh_dir),
            name=visual_spec.name,
            material=_build_material_from_urdf(visual_spec.material) if visual_spec.material is not None else None,
        )
        link.visuals.append(visual)
    for collision_spec in link_spec.collisions:
        if collision_spec.origin is None:
            origin = np.eye(4, dtype=np.float32)
        else:
            origin = collision_spec.origin
        collision = Collision(
            origin=origin,
            geometry=_build_geometry_from_urdf(collision_spec.geometry, mesh_dir=mesh_dir),
            name=collision_spec.name,
        )
        link.collisions.append(collision)
    return link


@dataclass
class KinematicsConfig:
    urdf_path: str
    device: torch.device

    joint_map: dict[str, Joint]
    link_map: dict[str, Link]

    base_link_name: str
    ee_link_names: list[str]
    active_joint_names: list[str]

    """
    if True, all kinematic chains will be calculated in parallel, otherwise
    sequentially (num_chains == 1). Parallel calculation is faster but requires
    more memory. Default is False.
    """
    parallel_chains: bool = False

    # inferred attributes
    num_dofs: int = field(init=False)
    num_chains: int = field(init=False)
    chains: list[list[str]] = field(init=False)

    """
    compact tensor spec (shape: 1 + num_chains + sum(chain_lengths) * 16)
    1. num_unique_links (shape: 1)
    2. num_chains (shape: 1)
    3. chain_lengths (shape: num_chains)
    4. chain_links (shape: sum(chain_lengths) x 16) 

    link/link's parent_joint spec (shape: 19)
    - joint_type (shape: 1)
    - active_joint_index (shape: 1, data range: [-1, num_dofs - 1], -1 for non-active joint)
    - parent_link_index_in_chain (shape: 1, data range: [-1, chain_lengths - 1], -1 for base link)
    - link_index_in_compact_tensor (shape: 1, data range: [-1, num_unique_links - 1], -1 for redundant link)
    - joint_origin (shape: 12)
    - joint_axis (shape: 3)
    """
    compact_tensor: Tensor = field(init=False)
    link_order_in_compact_tensor: list[str] = field(init=False)
    joint_limits: Tensor = field(init=False)

    def __post_init__(self):
        # infer number of DOFs
        self.num_dofs = len(self.active_joint_names)

        # infer chains
        if self.parallel_chains:
            chains = []
            for ee_link_name in self.ee_link_names:
                chain = []
                link_name = ee_link_name
                while link_name != self.base_link_name:
                    chain.append(link_name)
                    parent_joint_name = self.link_map[link_name].parent_joint_name
                    if parent_joint_name == NONE_JOINT_NAME:
                        raise ValueError(f"Non-base link {link_name} has no parent joint")
                    joint = self.joint_map[parent_joint_name]
                    link_name = joint.parent_link_name
                chain.append(self.base_link_name)
                chain.reverse()
                chains.append(chain)
            self.num_chains = len(self.ee_link_names)
            self.chains = chains
        else:
            # sort all links in topological order
            cur_links = [self.base_link_name]
            topological_order = []
            while cur_links:
                next_links = []
                for link_name in cur_links:
                    topological_order.append(link_name)
                    for joint in self.joint_map.values():
                        if joint.parent_link_name == link_name:
                            next_links.append(joint.child_link_name)
                cur_links = next_links
            self.num_chains = 1
            self.chains = [topological_order]

        # compute compact tensor and joint order
        self.compact_tensor, self.link_order_in_compact_tensor = self.compute_compact_tensor()

        # collect joint limits
        joint_limits = []
        for joint_name in self.active_joint_names:
            joint = self.joint_map[joint_name]
            if joint.limit is None:
                raise ValueError(f"Joint {joint_name} has no limit")
            joint_limits.append(joint.limit)
        self.joint_limits = torch.stack(joint_limits, dim=0)

    def compute_compact_tensor(self) -> tuple[Tensor, list[str]]:
        num_chains = torch.tensor([self.num_chains], dtype=torch.float32)  # cast to float32

        chain_lengths = torch.tensor([len(chain) for chain in self.chains], dtype=torch.float32)

        chain_links, link_order = [], []
        for chain in self.chains:
            for link_name in chain:
                joint_name = self.link_map[link_name].parent_joint_name
                joint = self.joint_map[joint_name]
                joint_type = torch.tensor([joint.type.value], dtype=torch.float32)
                if joint_name in self.active_joint_names:
                    active_joint_index = torch.tensor([self.active_joint_names.index(joint_name)], dtype=torch.float32)
                else:
                    active_joint_index = torch.tensor([-1], dtype=torch.float32)
                if link_name == self.base_link_name:
                    parent_link_index = torch.tensor([-1], dtype=torch.float32)
                else:
                    parent_link_index = torch.tensor([chain.index(joint.parent_link_name)], dtype=torch.float32)
                joint_origin = joint.origin[:3].reshape(-1)
                if link_name not in link_order:
                    link_order.append(link_name)
                    link_index_in_order = torch.tensor([len(link_order) - 1], dtype=torch.float32)
                else:
                    link_index_in_order = torch.tensor([-1], dtype=torch.float32)
                joint_tensor = torch.cat(
                    [
                        joint_type,
                        active_joint_index,
                        parent_link_index,
                        link_index_in_order,
                        joint_origin,
                        joint.axis,
                    ],
                    dim=0,
                )
                if joint_tensor.shape[0] != COMPACT_JOINT_SPEC_SIZE:
                    raise ValueError(f"Unexpected joint tensor shape: {joint_tensor.shape}")
                chain_links.append(joint_tensor)

        num_unique_links = torch.tensor([len(link_order)], dtype=torch.float32)
        compact_tensor = torch.cat([num_unique_links, num_chains, chain_lengths] + chain_links, dim=0).to(
            device=self.device
        )
        compact_tensor.requires_grad_(False)
        return compact_tensor, link_order

    def __str__(self) -> str:
        return repr(self)

    def __repr__(self) -> str:
        return f"KinematicsConfig(urdf_path={self.urdf_path}, num_dofs={self.num_dofs}, num_chains={self.num_chains})"

    @staticmethod
    def from_urdf(
        urdf_path: str,
        mesh_dir: str | None = None,
        base_link_name: str | None = None,
        ee_link_names: str | list[str] | None = None,
        parallel_chains: bool = False,
        device: torch.device | str | int = "cpu",
    ) -> "KinematicsConfig":
        """Parse URDF file and return kinematics configuration.

        Args:
            urdf_path (str): URDF file path.
            mesh_dir (str | None, optional): Directory containing mesh files. Defaults to None.
            base_link_name (str | None, optional): Base link name, will be inferred if not provided. Defaults to None.
            ee_link_names (str | list[str] | None, optional): End effector link names, will be inferred if not provided.
                Defaults to None.
            parallel_chains (bool, optional): If True, all kinematic chains will be calculated in parallel, otherwise
                sequentially (num_chains == 1). Parallel calculation is faster but requires more memory. Defaults to False.

        Returns:
            KinematicsConfig: Kinematics configuration.
        """
        if mesh_dir is None:
            mesh_dir = os.path.dirname(urdf_path)

        # parse URDF
        urdf = yourdfpy.URDF.load(
            urdf_path,
            load_meshes=False,
            build_scene_graph=False,
            mesh_dir=mesh_dir,
            filename_handler=yourdfpy.filename_handler_null,
        )
        # build joint maps
        joint_map: dict[str, Joint] = {
            joint_name: _build_joint_from_urdf(joint_spec) for joint_name, joint_spec in urdf.joint_map.items()
        }
        # infer active joint names (including all non-fixed joints)
        active_joint_names = [joint_name for joint_name, joint in joint_map.items() if joint.type != JointType.FIXED]
        # infer base link and ee links from joint map
        if base_link_name is None:
            link_names: list[str] = list(urdf.link_map.keys())
            for joint in joint_map.values():
                if joint.child_link_name in link_names:
                    link_names.remove(joint.child_link_name)
            if len(link_names) != 1:
                raise ValueError(f"Expected exactly one base link, got {len(link_names)}")
            base_link_name = link_names[0]
        if isinstance(ee_link_names, str):
            ee_link_names = [ee_link_names]
        elif ee_link_names is None:
            link_names = list(urdf.link_map.keys())
            for joint in joint_map.values():
                if joint.parent_link_name in link_names:
                    link_names.remove(joint.parent_link_name)
            if len(link_names) == 0:
                raise ValueError("Could not determine end effector link.")
            ee_link_names = link_names
        # add a none joint for base link
        joint_map[NONE_JOINT_NAME] = Joint(
            name=NONE_JOINT_NAME,
            type=JointType.NONE,
            origin=torch.eye(4, dtype=torch.float32),
            axis=torch.zeros(3, dtype=torch.float32),
            limit=torch.tensor([0.0, 0.0], dtype=torch.float32),
            parent_link_name="",
            child_link_name=base_link_name,
        )
        # build link maps
        link_map = {
            link_name: _build_link_from_urdf(link_spec, mesh_dir=mesh_dir)
            for link_name, link_spec in urdf.link_map.items()
        }
        # set parent joint names for links
        for joint_name, joint in joint_map.items():
            link_map[joint.child_link_name].set_parent_joint_name(joint_name)

        return KinematicsConfig(
            urdf_path=urdf_path,
            device=torch.device(device),
            joint_map=joint_map,
            link_map=link_map,
            active_joint_names=active_joint_names,
            base_link_name=base_link_name,
            ee_link_names=ee_link_names,
            parallel_chains=parallel_chains,
        )


__all__ = ["KinematicsConfig"]
