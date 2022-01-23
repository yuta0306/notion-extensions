from typing import Dict, Union

from .block import Block
from .children import Children

__all__ = [
    "Column",
    "ColumnList",
]


class Column(Block):
    """
    Column
    Column property values of block
    This must have at least one child

    Attributes
    ----------
    children : Children
        blocks in a single column

    Methods
    -------
    clear()
        Clear data of title
    json()
        Return this class as dictionary
    """

    TEMPLATE: Dict[str, Union[str, Dict]] = {
        "type": "column",
        "column": {},
    }

    def __init__(
        self,
        *block: Block,
    ):
        """
        Parameters
        ----------
        *block : Block
            blocks in a single column.
        """
        super().__init__()
        if len(block) < 1:
            raise ValueError("This must have at least one block")
        self.__children = Children(*block)
        self["column"] = self.__children

    @property
    def children(self) -> Children:
        return self.__children

    @children.setter
    def children(self, value: Children) -> None:
        self.__children = value
        self["column"] = self.__children


class ColumnList(Block):
    """
    Column
    Column property values of block
    This must have at least 2 columns

    Attributes
    ----------
    children : Children
        List of columns in the column_list block

    Methods
    -------
    clear()
        Clear data of title
    json()
        Return this class as dictionary
    """

    TEMPLATE: Dict[str, Union[str, Dict]] = {
        "type": "column_list",
        "column_list": {},
    }

    def __init__(
        self,
        *column: Column,
    ):
        """
        Parameters
        ----------
        *column : Column
            columns in the column_list block.
        """
        super().__init__()
        if len(column) < 2:
            raise ValueError("This must have at least 2 columns")
        self.__children = Children(*column)
        self["column_list"] = self.__children

    @property
    def children(self) -> Children:
        return self.__children

    @children.setter
    def children(self, value: Children) -> None:
        self.__children = value
        self["column_list"] = self.__children
