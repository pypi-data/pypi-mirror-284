from __future__ import annotations

import numpy as np
import torch
import trimesh
from torch import Tensor

from fastdev.geom.point_mesh import C
from fastdev.utils.struct_utils import list_to_packed


class Meshes:
    _INTERNAL_TENSORS: list[str] = [
        "_verts_packed",
        "_verts_packed_to_mesh_idx",
        "_mesh_to_verts_packed_first_idx",
        "_num_verts_per_mesh",
        "_faces_packed",
        "_faces_packed_to_mesh_idx",
        "_mesh_to_faces_packed_first_idx",
        "_num_faces_per_mesh",
    ]

    def __init__(
        self, verts: Tensor | list[Tensor], faces: Tensor | list[Tensor], device: torch.device | str | int | None = None
    ):
        if isinstance(verts, list) and isinstance(faces, list):
            self._verts_list, self._faces_list = verts, faces
        elif isinstance(verts, Tensor) and isinstance(faces, Tensor):
            self._verts_list, self._faces_list = [verts], [faces]
        else:
            raise ValueError("verts and faces should be both list or both Tensor.")

        if device is not None:
            self._verts_list = [v.to(device=device) for v in self._verts_list]
            self._faces_list = [f.to(device=device) for f in self._faces_list]
        self._device = self._verts_list[0].device

        self._num_verts_per_mesh = torch.tensor(
            [v.shape[0] for v in self._verts_list], dtype=torch.long, device=self._device
        )
        self._num_faces_per_mesh = torch.tensor(
            [f.shape[0] for f in self._faces_list], dtype=torch.long, device=self._device
        )

        verts_list_to_packed = list_to_packed(self._verts_list)
        self._verts_packed = verts_list_to_packed[0]
        if not torch.allclose(self._num_verts_per_mesh, verts_list_to_packed[1]):
            raise ValueError("The number of verts per mesh should be consistent.")
        self._mesh_to_verts_packed_first_idx = verts_list_to_packed[2]
        self._verts_packed_to_mesh_idx = verts_list_to_packed[3]

        faces_list_to_packed = list_to_packed(self._faces_list)
        faces_packed = faces_list_to_packed[0]
        if not torch.allclose(self._num_faces_per_mesh, faces_list_to_packed[1]):
            raise ValueError("The number of faces per mesh should be consistent.")
        self._mesh_to_faces_packed_first_idx = faces_list_to_packed[2]
        self._faces_packed_to_mesh_idx = faces_list_to_packed[3]
        faces_packed_offset = self._mesh_to_verts_packed_first_idx[self._faces_packed_to_mesh_idx]
        self._faces_packed = faces_packed + faces_packed_offset.view(-1, 1)

    @staticmethod
    def from_files(filenames: str | list[str], device: torch.device | str | int | None = None) -> Meshes:
        if isinstance(filenames, str):
            filenames = [filenames]
        verts, faces = [], []
        for filename in filenames:
            mesh: trimesh.Trimesh = trimesh.load(filename, force="mesh", process=False)  # type: ignore
            verts.append(torch.from_numpy(mesh.vertices.astype(np.float32)))
            faces.append(torch.from_numpy(mesh.faces))
        return Meshes(verts, faces, device=device)

    def closest_points_on_mesh(self, query_points_list: list[Tensor]) -> tuple[Tensor, Tensor, Tensor]:
        points_list_to_packed = list_to_packed(query_points_list)
        points_packed = points_list_to_packed[0]
        points_first_idx = points_list_to_packed[2]
        max_points_per_batch = max(p.shape[0] for p in query_points_list)

        return C.closest_point_on_mesh(
            points_packed,
            points_first_idx,
            self._verts_packed[self._faces_packed],
            self._mesh_to_faces_packed_first_idx,
            max_points_per_batch,
            5e-3,
        )

    def clone(self) -> Meshes:
        verts_list = self._verts_list
        faces_list = self._faces_list
        new_verts_list = [v.clone() for v in verts_list]
        new_faces_list = [f.clone() for f in faces_list]
        other = self.__class__(verts=new_verts_list, faces=new_faces_list)
        for k in self._INTERNAL_TENSORS:
            v = getattr(self, k)
            if torch.is_tensor(v):
                setattr(other, k, v.clone())
        return other

    def to(self, device: torch.device | str | int) -> Meshes:
        for i in range(len(self._verts_list)):
            self._verts_list[i] = self._verts_list[i].to(device=device)
            self._faces_list[i] = self._faces_list[i].to(device=device)
        other = self.clone()
        other._verts_list = [v.to(device=device) for v in self._verts_list]
        other._faces_list = [f.to(device=device) for f in self._faces_list]
        for k in self._INTERNAL_TENSORS:
            v = getattr(self, k)
            if torch.is_tensor(v):
                setattr(other, k, v.to(device=device))
        return other


if __name__ == "__main__":
    from fastdev import Timer
    from fastdev.io.download import cached_local_path

    mesh_path = cached_local_path(
        "https://raw.githubusercontent.com/alecjacobson/common-3d-test-models/master/data/stanford-bunny.obj",
        rel_cache_path="common-meshes/bunny.obj",
    )
    with Timer("Creating meshes"):
        meshes = Meshes.from_files(mesh_path, device="cuda")

    g = torch.Generator()
    g.manual_seed(0)
    query_points = [torch.randn(2000, 3, generator=g).to(torch.float32)]
    query_points = [p.to("cuda") for p in query_points]

    with Timer("Finding closest points on mesh"):
        closest_points, normals, distances = meshes.closest_points_on_mesh(query_points)
