from typing import Dict, List, Union

from .block import Block

__all__ = [
    "Children",
]


class Children(Block):
    """
    Children
    Children property values of block

    Attributes
    ----------

    Methods
    -------
    clear()
        Clear data of title
    json()
        Return this class as dictionary
    
    Usage
    -----
    >>> from notion_extensions.base.props.block import Children 
    >>> Children()
    {'children': []}
    
    """

    TEMPLATE: Dict[str, List[Block]] = {"children": []}

    def __init__(
        self,
        *block: Block,
    ):
        super().__init__()
        self.__blocks = list(block)
        self["children"] = self.__blocks

    def __add__(self, other: Union[Block, List[Block]]):
        if isinstance(other, list):
            self.extend(other)
            return self
        self.append(other)
        return self

    def __iadd__(self, other: Union[Block, List[Block]]):
        return self.__add__(other)

    def append(self, block: Block) -> None:
        """
        append(block: Block)
            Append Block to existing list of Block

        Parameters
        ----------
        block : Block
            Block you append to Children
        """
        self.__blocks.append(block)
        self["children"] = self.__blocks

    def extend(self, blocks: List[Block]) -> None:
        """
        extens(blocks: List[Block])
            Append Block to existing list of Block

        Parameters
        ----------
        blocks : list of Block
            List of block you append to Children
        """
        self.__blocks.extend(blocks)
        self["children"] = self.__blocks

    def insert(self, index: int, block: Block) -> None:
        """
        insert(index: int, block: Block)
            Append block to existing list of Block

        Parameters
        ----------
        index : int
            Index you insert Block into Children
        block : Block
            Block you insert into Children
        """
        self.__blocks.insert(index, block)
        self["children"] = self.__blocks

    def pop(self, index=None):
        """
        pop(Block: Block)
            Pop Block to existing list of Block

        Parameters
        ----------
        index : int, default=None
            Block you pop from RichBlock
        """
        item = self.__blocks.pop(index)
        self["children"] = self.__blocks
        return item
