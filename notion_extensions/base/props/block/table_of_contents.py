from typing import Dict, Union

from .block import Block

__all__ = [
    "TableOfContents",
]


class TableOfContents(Block):
    """
    TableOfContents
    TableOfContents property values of block

    Attributes
    ----------

    Methods
    -------
    clear()
        Clear data of title
    json()
        Return this class as dictionary
    """

    TEMPLATE: Dict[str, Union[str, Dict]] = {
        "type": "table_of_contents",
        "table_of_contents": {},
    }

    def __init__(self):
        super().__init__()
