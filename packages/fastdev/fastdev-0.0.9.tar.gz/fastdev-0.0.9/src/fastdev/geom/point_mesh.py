from __future__ import annotations

import glob
import os
import shutil
from typing import Any

from torch.utils.cpp_extension import _get_build_directory, load

from fastdev.utils.tui import console
from fastdev.constants import FDEV_CSRC_ROOT
from fastdev.utils import Timer
from fastdev.utils.cuda import cuda_toolkit_available, current_cuda_arch

os.environ["TORCH_CUDA_ARCH_LIST"] = current_cuda_arch()

name = "fastdev_point_mesh"
build_dir = _get_build_directory(name, verbose=False)
extra_include_paths: list[str] = [FDEV_CSRC_ROOT]
extra_cflags = ["-O3", "-DWITH_CUDA"]
extra_cuda_cflags = ["-O3", "-DWITH_CUDA"]

C: Any = None

sources = []
for ext in ["cpp", "cu"]:
    sources.extend(glob.glob(os.path.join(FDEV_CSRC_ROOT, "point_mesh", f"**/*.{ext}"), recursive=True))


# if failed, try with JIT compilation
if cuda_toolkit_available():
    if os.listdir(build_dir) != []:
        # If the build exists, we assume the extension has been built
        # and we can load it.
        with Timer("Loading extension"):
            C = load(
                name=name,
                sources=sources,
                extra_cflags=extra_cflags,
                extra_cuda_cflags=extra_cuda_cflags,
                extra_include_paths=extra_include_paths,
            )
    else:
        # Build from scratch. Remove the build directory just to be safe: pytorch jit might stuck
        # if the build directory exists.
        shutil.rmtree(build_dir, ignore_errors=True)
        with Timer("Building extension"), console.status(
            "[bold yellow]Building extension (This may take a few minutes the first time)",
            spinner="bouncingBall",
        ):
            C = load(
                name=name,
                sources=sources,
                extra_cflags=extra_cflags,
                extra_cuda_cflags=extra_cuda_cflags,
                extra_include_paths=extra_include_paths,
            )
else:
    console.print("[yellow]No CUDA toolkit found. NeuralTeleop will be disabled.[/yellow]")
