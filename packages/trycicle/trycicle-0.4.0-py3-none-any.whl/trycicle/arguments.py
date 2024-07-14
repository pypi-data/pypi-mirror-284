import dataclasses
import os
import pathlib
import typing
from functools import cached_property

import platformdirs

from .variables import Variables, get_predefined_variables

DebugEnabled = typing.Literal["true", "false", "immediate"]


@dataclasses.dataclass
class Arguments:
    original_dir: str = ""
    service_logs: bool = False
    debugger: DebugEnabled = "false"
    cache_directory: str = ""

    def __post_init__(self) -> None:
        self.original_dir = os.path.abspath(self.original_dir)
        if not self.cache_directory:
            self.cache_directory = platformdirs.user_cache_dir("trycicle")

    @property
    def interactive(self) -> bool:
        return self.debugger != "false"

    @property
    def cache_path(self) -> pathlib.Path:
        return pathlib.Path(self.cache_directory)

    @cached_property
    def variables(self) -> Variables:
        return get_predefined_variables(self.original_dir)

    def without_variables(self) -> typing.Self:
        copy = dataclasses.replace(self)
        copy.__dict__["variables"] = Variables({})
        return copy
