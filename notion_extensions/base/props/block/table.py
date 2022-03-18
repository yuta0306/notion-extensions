from typing import Dict, List, Union

from ..common import RichText
from .block import Block
from .children import Children

__all__ = [
    "TableRow",
    "Table",
]


class TableRow(Block):
    """
    TableRow
    TableRow property values of block

    Attributes
    ----------
    cells : list of list of RichText
        Array of cell contents in horizontal display order.
        Each cell itself is an array of rich text objects

    Methods
    -------
    clear()
        Clear data of title
    json()
        Return this class as dictionary
    """

    TEMPLATE: Dict[str, Union[str, Dict]] = {
        "type": "table_row",
        "table_row": {
            "cells": [],
        },
    }

    def __init__(
        self,
        *cell: RichText,
    ):
        """
        Parameters
        ----------
        *cell : RichText
            Array of cell contents in horizontal display order.
            Each cell itself is an array of rich text objects
        """
        super().__init__()
        for c in cell:
            self["table_row"]["cells"].append(c[c.key])

    def __add__(self, other: Union[RichText, List[RichText]]):
        if isinstance(other, list):
            self.extend(other)
            return self
        self.append(other)
        return self

    def __iadd__(self, other: Union[RichText, List[RichText]]):
        return self.__add__(other)

    def __len__(self):
        return len(self["table_row"]["cells"])

    @property
    def cells(self) -> List[List[Dict]]:
        return self["table_row"]["cells"]

    @cells.deleter
    def cells(self) -> None:
        while len(self["table_row"]["cells"]) > 0:
            _ = self["table_row"]["cells"].pop()

    def append(self, cell: RichText) -> None:
        """
        append(cell: RichText)
            Append RichText to existing cells

        Parameters
        ----------
        cell : RichText
            RichText you append to cells
        """
        self["table_row"]["cells"].append(cell[cell.key])

    def extend(self, cells: List[RichText]) -> None:
        """
        extens(cells: List[RichText])
            Append RichText to existing cells

        Parameters
        ----------
        cells : list of RichText
            List of RichText you append to cells
        """
        for cell in cells:
            self["table_row"]["cells"].append(cell[cell.key])

    def insert(self, index: int, cell: RichText) -> None:
        """
        insert(index: int, cell: RichText)
            Append RichText to existing cells

        Parameters
        ----------
        index : int
            Index you insert Text into
        cell : RichText
            RichText you insert into cells
        """
        self["table_row"]["cells"].insert(index, cell[cell.key])

    def pop(self, index=None):
        """
        pop(index: int)
            Pop cell from existing cells

        Parameters
        ----------
        index : int, default=None
            Index of cell you pop
        """
        self["table_row"]["cells"].pop(index)


class Table(Block):
    """
    Table
    Table property values of block
    Tables are parent blocks for table row children. They can only contain children of type table_row.
    When creating a table block via the Append block children endpoint,
    the table must have at least 1 table_row whose cells array has the same length as the table_width

    Attributes
    ----------
    table_width : int
        Number of columns in the table.
        Note that this cannot be changed via the public API once a table is created
    children : Children
        table row children
    has_column_header : bool, default=False
        Whether or not the table has a column header.
        If true, the first row in the table will appear visually distinct from the other rows.
    has_row_header : bool, default=False
        Whether or not the table has a header row.
        If true, the first column in the table will appear visually distinct from the other columns.

    Methods
    -------
    clear()
        Clear data of title
    json()
        Return this class as dictionary
    """

    TEMPLATE: Dict[str, Union[str, Dict]] = {
        "type": "table",
        "table": {
            "table_width": 1,
            "has_column_header": False,
            "has_row_header": False,
        },
    }

    def __init__(
        self,
        table_width: int,
        *table_row: TableRow,
        has_column_header: bool = False,
        has_row_header: bool = False,
    ):
        """
        Parameters
        ----------
        table_width : int
            Number of columns in the table.
            Note that this cannot be changed via the public API once a table is created
        *table_row : TableRow
            table row children
        has_column_header : bool, default=False
            Whether or not the table has a column header.
            If true, the first row in the table will appear visually distinct from the other rows.
        has_row_header : bool, default=False
            Whether or not the table has a header row.
            If true, the first column in the table will appear visually distinct from the other columns.
        """
        super().__init__()
        for table_row_ in table_row:  # Validate length of table row
            if len(table_row_) != table_width:
                raise ValueError(
                    "table_width must be equal to table_row size, "
                    f"expected {table_width} but {len(table_row_)} is given"
                )
        self["table"]["table_width"] = table_width
        self["table"]["has_column_header"] = has_column_header
        self["table"]["has_row_header"] = has_row_header
        self.__children = Children(*table_row)
        self["table"].update(self.__children)

    @property
    def table_width(self) -> int:
        return self["table"]["table_width"]

    @property
    def has_column_header(self) -> bool:
        return self["table"]["has_column_header"]

    @has_column_header.setter
    def has_column_header(self, value: bool) -> None:
        self["table"]["has_column_header"] = value

    @property
    def has_row_header(self) -> bool:
        return self["table"]["has_row_header"]

    @has_row_header.setter
    def has_row_header(self, value: bool) -> None:
        self["table"]["has_column_header"] = value

    @property
    def children(self) -> Children:
        return self.__children

    @children.setter
    def children(self, value: Children) -> None:
        self.__children = value
        self["table"].update(self.__children)

    @children.deleter
    def children(self) -> None:
        self.__children = Children()
        self["table"].update(self.__children)
