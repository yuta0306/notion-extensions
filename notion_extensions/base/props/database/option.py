import sys

if sys.version_info > (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info > (3, 9):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

from ..common import BaseProps

__all__ = [
    "Option",
]

AVAILABLE_COLOR: TypeAlias = Literal[
    "gray",
    "brown",
    "orange",
    "yellow",
    "green",
    "blue",
    "purple",
    "pink",
    "red",
]


class Option(BaseProps):
    TEMPLATE = {
        "name": "",
        "color": "",
    }

    def __init__(self, name: str, color: AVAILABLE_COLOR):
        super().__init__()
        self["name"] = name
        self["color"] = color

    @property
    def name(self) -> str:
        return self["name"]

    @name.setter
    def name(self, value: str) -> None:
        self["name"] = value

    @property
    def color(self) -> AVAILABLE_COLOR:
        return self["color"]

    @color.setter
    def color(self, value: AVAILABLE_COLOR) -> None:
        self["color"] = value
