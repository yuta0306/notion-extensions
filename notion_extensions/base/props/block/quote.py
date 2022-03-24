from typing import Dict, Optional, Union

from ..common import RichText, Text
from .block import Block
from .children import Children

__all__ = [
    "Quote",
]


class Quote(Block):
    """
    Quote
    Quote property values of block

    Attributes
    ----------
    text : RichText
        text
    children : Children
        children

    Methods
    -------
    clear()
        Clear data of title
    json()
        Return this class as dictionary
    Usage
    -----
    >>> from notion_extensions.base.props.block import Quote
    >>> Quote()
    {'type': 'quote', 'quote': {'rich_text': []}}

    """

    TEMPLATE: Dict[str, Union[str, Dict]] = {
        "type": "quote",
        "quote": {
            "rich_text": [],
        },
    }

    def __init__(
        self,
        *text: Union[Text, RichText],
        children: Optional[Children] = None,
    ):
        """
        Parameters
        ----------
        *text : Text or RichText
            text
        children : Children, optional
            children
        """
        super().__init__()
        base = []  # Aggregate Texts
        for t in text:
            if isinstance(t, RichText):
                base.extend(list(t[t.key]))
            elif isinstance(t, Text):
                base.append(t)
            else:
                raise ValueError(
                    f"Expected type is `RichText` or `Text`, but {type(t)} is given"
                )
        self.__text = RichText(key="rich_text", *base)
        self["quote"].update(self.__text)  # Add Texts with RichText Style
        if children is not None:
            self["quote"].update(children)  # if children exists, Add Chilren

    @property
    def text(self) -> RichText:
        return self.__text

    @text.setter
    def text(self, value: RichText) -> None:
        if value.key != "rich_text":
            raise ValueError("RichText's key is must be `text`")
        self.__text = value
        self["quote"].update(self.__text)

    @property
    def children(self) -> Children:
        return self["quote"]["children"]

    @children.setter
    def children(self, value: Children) -> None:
        self["quote"].update(value)
