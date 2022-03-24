from typing import Dict, Union

from .block import Block
from .children import Children

__all__ = [
    "OriginalSynced",
    "ReferenceSynced",
]


class OriginalSynced(Block):
    """
     OriginalSynced
     OriginalSynced property values of block
     To create a synced_block, the developer needs to create an original synced block.
     Developers will be able to identify the original synced_block because it does not "sync_from" any other block
     (synced_from property is set to null)

    Attributes
    ----------
    children : Children
        Any nested children blocks of the synced_block block.
        These blocks will be synced across this block and references to this synced_block

    Methods
    -------
    clear()
        Clear data of title
    json()
        Return this class as dictionary

    Usage
    -----
    >>> from notion_extensions.base.props.block import OriginalSynced
    >>> OriginalSynced()
    {'type': 'synced_block', 'synced_block': {'synced_from': None, 'children': []}}

    """

    TEMPLATE: Dict[str, Union[str, Dict]] = {
        "type": "synced_block",
        "synced_block": {
            "synced_from": None,
        },
    }

    def __init__(
        self,
        *child: Block,
    ):
        """
        Parameters
        ----------
        *child : Block
            Any nested children blocks of the synced_block block.
            These blocks will be synced across this block and references to this synced_block
        """
        super().__init__()
        self.__children = Children(*child)
        self["synced_block"].update(self.__children)

    @property
    def children(self) -> Children:
        return self.__children

    @children.setter
    def children(self, children: Children) -> None:
        self.__children = children
        self["synced_block"].update(self.__children)


class ReferenceSynced(Block):
    """
    ReferenceSynced
    ReferenceSynced property values of block
    To sync the content of the original synced_block with another synced_block,
    the developer simply needs to refer to that synced_block using the synced_from property

    Attributes
    ----------
    block_id : str
        Identifier of an original synced_block

    Methods
    -------
    clear()
        Clear data of title
    json()
        Return this class as dictionary
    """

    TEMPLATE: Dict[str, Union[str, Dict]] = {
        "type": "synced_block",
        "synced_block": {
            "synced_from": {
                "block_id": "",
            },
        },
    }

    def __init__(
        self,
        block_id: str,
    ):
        """
        Parameters
        ----------
        block_id : str
            Identifier of an original synced_block
        """
        super().__init__()
        self["synced_block"]["synced_from"]["block_id"] = block_id

    @property
    def block_id(self) -> str:
        return self["synced_block"]["synced_from"]["block_id"]

    @block_id.setter
    def block_id(self, block_id: str) -> None:
        self["synced_block"]["synced_from"]["block_id"] = block_id

    @block_id.deleter
    def block_id(self) -> None:
        self["synced_block"]["synced_from"]["block_id"] = ""
