from typing import List, Union

from ..common import BaseProps
from .option import Option

__all__ = [
    "Select",
]


class Select(BaseProps):
    """
    Select database property objects

    Attributes
    ----------
    key : str
        The name of the property as it appears in Notion.
    """

    def __init__(self, key: str, *option: Option):
        """
        Select database property objects

        Parameters
        ----------
        key : str
            The name of the property as it appears in Notion.
        *option : Option
            Sorted list of options available for this property.

        Usage
        -----
        >>> from notion_extensions.base.props.database import Option, Select
        >>> option1 = Option(name="option 1")
        >>> option2 = Option(name="option 2", color="red")
        >>> select = Select("options", option1, option2)
        >>> select
        {
            'options': {
                'select': {
                    'options': [
                        {'name': 'option 1', 'color': 'default'},
                        {'name': 'option 2', 'color': 'red'}
                    ]
                }
            }
        }
        >>>
        """
        super().__init__()
        self.__key = key
        self[key] = {
            "select": {
                "options": list(option),
            },
        }

    @property
    def key(self) -> str:
        return self.__key

    def __add__(self, other: Union[Option, List[Option]]):
        if isinstance(other, list):
            self[self.__key]["select"]["options"].extend(other)
            return self
        self[self.__key]["select"]["options"].append(other)
        return self

    def __iadd__(self, other: Union[Option, List[Option]]):
        self.__add__(other)
        return self

    def append(self, option: Option):
        self[self.__key]["select"]["options"].append(option)

    def extend(self, options: List[Option]):
        self[self.__key]["select"]["options"].extend(options)

    def insert(self, option: Option, index: int):
        self[self.__key]["select"]["options"].insert(option, index)
