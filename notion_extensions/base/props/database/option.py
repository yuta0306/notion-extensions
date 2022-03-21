import sys

if sys.version_info > (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

from ..common import BaseProps

__all__ = [
    "Option",
]

AVAILABLE_COLOR: TypeAlias = Literal[
    "default",
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
    """
    Attributes
    ----------
    name : str
        Name of the option as it appears in Notion.
        Note: Commas (",") are not valid for select values.
    color : AVAILABLE_COLOR
        Color of the option.
        Possible values include: default, gray, brown, orange, yellow, green, blue, purple, pink, red.
    """

    TEMPLATE = {
        "name": "",
        "color": "",
    }

    def __init__(self, name: str, color: AVAILABLE_COLOR = "default"):
        """
        Parameters
        ----------
        name : str
        Name of the option as it appears in Notion.
            Note: Commas (",") are not valid for select values.
        color : AVAILABLE_COLOR
            Color of the option.
            Possible values include: default, gray, brown, orange, yellow, green, blue, purple, pink, red.

        Raises
        ------
        ValueError
            Commas `,` are given as name

        Usage
        -----
        >>> from notion_extensions.base.props.database import Option
        >>> option = Option(name="option 1", color="red")
        >>> option
        {'name': 'option 1', 'color': 'red'}
        """
        super().__init__()
        if "," in name:
            raise ValueError("Note: Commas `,` are not valid for select values.")
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
