import torch
from fastdev.robo.robot_model import RobotModel


def test_robot_model():
    device = "cpu"
    robot_model = RobotModel("assets/panda.urdf", device)
    assert robot_model.num_dofs == 9
    joint_values = torch.tensor([[0.1, 0.2, 0.3, -0.5, 0.1, 0.2, 0.3, 0.02, 0.02]], dtype=torch.float32, device=device)
    joint_values.requires_grad_(True)
    joint_poses = robot_model.forward_kinematics(joint_values)

    expected_joint_pose = torch.tensor(
        [
            [0.4639, 0.7548, -0.4637, 0.2874],
            [0.8131, -0.5706, -0.1155, 0.1212],
            [-0.3518, -0.3235, -0.8784, 0.7954],
            [0.0000, 0.0000, 0.0000, 1.0000],
        ],
        device=device,
    )
    assert torch.allclose(joint_poses[0, -1], expected_joint_pose, atol=1e-4)

    joint_poses[:, -2, :3, 3].abs().sum().backward()
    joint_values_grad = joint_values.grad.clone()  # type: ignore
    expected_grad = torch.tensor(
        [[0.2193, 0.1663, 0.1481, -0.0204, 0.0791, 0.2665, -0.0185, -0.1392, 0.0000]], device=device
    )
    assert torch.allclose(joint_values_grad, expected_grad, atol=1e-4)

    if torch.cuda.is_available():
        device = "cuda"
        robot_model = RobotModel("assets/panda.urdf", device)
        joint_values = torch.tensor(
            [[0.1, 0.2, 0.3, -0.5, 0.1, 0.2, 0.3, 0.02, 0.02]], dtype=torch.float32, device=device
        )
        joint_values.requires_grad_(True)
        joint_poses = robot_model.forward_kinematics(joint_values)

        expected_joint_pose = torch.tensor(
            [
                [0.4639, 0.7548, -0.4637, 0.2874],
                [0.8131, -0.5706, -0.1155, 0.1212],
                [-0.3518, -0.3235, -0.8784, 0.7954],
                [0.0000, 0.0000, 0.0000, 1.0000],
            ],
            device=device,
        )
        assert torch.allclose(joint_poses[0, -1], expected_joint_pose, atol=1e-4)

        joint_poses[:, -2, :3, 3].abs().sum().backward()
        joint_values_grad = joint_values.grad.clone()  # type: ignore
        expected_grad = torch.tensor(
            [[0.2193, 0.1663, 0.1481, -0.0204, 0.0791, 0.2665, -0.0185, -0.1392, 0.0000]], device=device
        )
        assert torch.allclose(joint_values_grad, expected_grad, atol=1e-4)

    device = "cuda" if torch.cuda.is_available() else "cpu"
    robot_model = RobotModel("assets/kuka_iiwa.urdf", device)
    joint_values = torch.tensor([[0.1, 0.2, 0.3, 0.1, 0.2, 0.3, 0.1]], dtype=torch.float32, device=device)
    joint_values.requires_grad_(True)
    joint_poses = robot_model.forward_kinematics(joint_values)

    expected_joint_pose = torch.tensor(
        [
            [-0.8229, 0.5582, 0.1066, 0.1027],
            [-0.5629, -0.8263, -0.0190, 0.0048],
            [0.0775, -0.0756, 0.9941, 0.9550],
            [0.0000, 0.0000, 0.0000, 1.0000],
        ],
        device=device,
    )
    assert torch.allclose(joint_poses[0, -3], expected_joint_pose, atol=1e-4)

    joint_poses[:, -1, :3, :3].abs().sum().backward()
    joint_values_grad = joint_values.grad.clone()  # type: ignore
    expected_grad = torch.tensor([[0.4059, 1.4686, 0.3498, -1.4969, 0.3350, 1.4344, 0.4556]], device=device)
    assert torch.allclose(joint_values_grad, expected_grad, atol=1e-4)
