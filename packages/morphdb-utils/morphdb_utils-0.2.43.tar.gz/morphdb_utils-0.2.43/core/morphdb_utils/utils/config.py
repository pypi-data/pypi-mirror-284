# type: ignore
# TODO: このファイルは将来的に削除して、呼び出し元ではmorph.pyの共通処理を利用する

from __future__ import annotations

import os
from typing import Dict, List, Optional, Tuple, TypedDict

import yaml


class Resource(TypedDict, total=False):
    path: str
    connection: Optional[str]
    storage_path: Optional[str]
    output_paths: Optional[List[str]] = None
    public: Optional[bool] = False


class Coordinates(TypedDict):
    x: int
    y: int
    w: int
    h: int


class Job(TypedDict):
    name: str
    schedule: str
    timezone: str


class CanvasAlias(TypedDict):
    coordinates: Coordinates
    parents: Optional[List[str]]


class Canvas(TypedDict, total=False):
    jobs: Optional[Job]
    cells: Dict[str, CanvasAlias]


class Config(TypedDict):
    version: str
    resources: Dict[str, Resource]
    canvases: Dict[str, Canvas]


MORPH_CONFIG_NAME = "morph.yaml"


class MorphConfig:
    def __init__(self):
        def find(start_dir: str) -> Tuple[str, Dict]:
            current_dir = start_dir
            while True:
                morph_config_path = os.path.join(current_dir, MORPH_CONFIG_NAME)
                if os.path.isfile(morph_config_path):
                    with open(morph_config_path, encoding="utf-8") as f:
                        config = yaml.safe_load(f)
                    return os.path.dirname(morph_config_path), config

                parent_dir = os.path.dirname(current_dir)
                if current_dir == parent_dir:
                    break

                current_dir = parent_dir
            return None

        current_dir = os.getcwd()

        config_path, config = find(current_dir)
        if config_path is None or config is None:
            raise Exception("morph.yaml not found")

        self.config = Config(**config)
        self.config_path = config_path

    def get_config(self) -> Config:
        return self.config

    def get_config_path(self) -> str:
        return self.config_path

    def get_filepath(self, alias: str) -> Optional[str]:
        resource = self.config["resources"].get(alias)
        resource_path = resource["path"] if resource and "path" in resource else None
        if resource_path.startswith(self.config_path):
            return resource_path
        return os.path.join(self.config_path, os.path.relpath(resource["path"]))

    def get_connection(self, alias: str) -> Optional[str]:
        resource = self.config["resources"].get(alias)
        return resource["connection"] if resource and "connection" in resource else None

    def get_alias(self, abs_path: str) -> str:
        for alias, resource in self.config["resources"].items():
            resource_path = (
                resource["path"] if resource and "path" in resource else None
            )
            if resource_path.startswith(self.config_path):
                pass
            else:
                resource_path = os.path.join(
                    self.config_path, os.path.relpath(resource["path"])
                )
            if resource_path == abs_path:
                return alias
        return None

    def get_output_path(self, alias: str) -> Optional[str]:
        resource = self.config["resources"].get(alias)
        # default output path(/path/to/config/data/outputs/{alias})
        output_paths = (
            resource["output_paths"]
            if resource and "output_paths" in resource
            else None
        )
        if (output_paths is not None and len(output_paths) < 1) or output_paths is None:
            tmp_path = os.path.join(self.config_path, "data", "outputs", f"{alias}")
            if os.path.exists(tmp_path):
                return tmp_path
            tmp_path = os.path.join(
                self.config_path, "src", "data", "outputs", f"{alias}"
            )
            if os.path.exists(tmp_path):
                return tmp_path
            return None
        elif not output_paths[0].startswith(self.config_path):
            return os.path.join(self.config_path, os.path.realpath(output_paths[0]))

        return (
            output_paths[0]
            if output_paths[0] is not None
            else os.path.join(self.config_path, "data", "outputs", f"{alias}")
        )

    @staticmethod
    def get_cell_type(filepath: str) -> str:
        ext = os.path.splitext(filepath)[1][1:]
        if ext == "sql":
            return "sql"
        elif ext == "py":
            return "python"
        elif ext == "":
            return "directory"
        else:
            return "file"
