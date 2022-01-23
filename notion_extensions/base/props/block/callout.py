from typing import Dict, Optional, Union

from .block import Block
from .children import Children
from ..common import Emoji, Icon, Text, RichText

__all__ = [
    "Callout",
]


class Callout(Block):
    """
    Callout
    Callout property values of block

    Attributes
    ----------
    text : RichText
        text
    icon : Icon
        icon
    children : Children
        children

    Methods
    -------
    clear()
        Clear data of title
    json()
        Return this class as dictionary
    """

    TEMPLATE: Dict[str, Union[str, Dict]] = {
        "type": "callout",
        "callout": {
            "text": [],
        },
    }

    def __init__(
        self,
        *text: Union[Text, RichText],
        icon: Icon = Icon(Emoji("")),
        children: Optional[Children] = None,
    ):
        """
        Parameters
        ----------
        *text : Text or RichText
            text
        icon : Icon, defalut=Icon(Emoji(""))
            icon
        children : Children, optional
            children
        """
        super().__init__()
        self["callout"].update(icon)  # Add Icon
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
        self.__text = RichText(key="text", *base)
        self["callout"].update(self.__text)  # Add Texts with RichText Style
        if children is not None:
            self["callout"].update(children)  # if children exists, Add Chilren

    @property
    def text(self) -> RichText:
        return self.__text

    @text.setter
    def text(self, value: RichText) -> None:
        if value.key != "text":
            raise ValueError("RichText's key is must be `text`")
        self.__text = value
        self["callout"].update(self.__text)

    @property
    def icon(self) -> Icon:
        return self["callout"]["icon"]

    @icon.setter
    def icon(self, value: Icon) -> None:
        self["callout"].update(value)

    @property
    def children(self) -> Children:
        return self["callout"]["children"]

    @children.setter
    def children(self, value: Children) -> None:
        self["callout"].update(value)
