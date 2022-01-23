from typing import List, Union

from ..common import BaseProps
from .option import Option

__all__ = [
    "Select",
]


class Select(BaseProps):
    def __init__(self, key: str, *option: Option):
        super().__init__()
        self.key = key
        self[key] = {
            "select": {
                "options": list(option),
            },
        }

    def __add__(self, other: Union[Option, List[Option]]):
        if isinstance(other, list):
            self[self.key]["select"]["options"].extend(other)
            return self
        self[self.key]["select"]["options"].append(other)
        return self

    def __iadd__(self, other: Union[Option, List[Option]]):
        self.__add__(other)
        return self

    def append(self, option: Option):
        self[self.key]["select"]["options"].append(option)

    def extend(self, options: List[Option]):
        self[self.key]["select"]["options"].extend(options)

    def insert(self, option: Option, index: int):
        self[self.key]["select"]["options"].insert(option, index)
