import os
import sys
from pathlib import Path
from typing import TypedDict


def safe_path(root_path: Path, input_path: Path) -> Path:
    """
    How to prevent directory traversal attack from Python code
    https://stackoverflow.com/a/45190125
    """
    resolved_path = root_path.joinpath(input_path).resolve()
    if not resolved_path.is_relative_to(root_path.resolve()):
        raise ValueError(f"Path {input_path} is not relative to {root_path}")
    return resolved_path.relative_to(root_path.resolve())


def safe_path_join(root: Path, *paths: Path | str) -> Path:
    return root / safe_path(root, root.joinpath(*paths))


class LaunchCommand(TypedDict):
    cwd: str
    args: list[str]


def get_launch_command() -> LaunchCommand:
    args = [sys.executable, "-m", "omuserver", *sys.argv[1:]]
    return {
        "cwd": os.getcwd(),
        "args": args,
    }
