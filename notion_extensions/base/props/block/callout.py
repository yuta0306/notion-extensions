from typing import Dict, Optional, Union

from ..common import Emoji, Icon, RichText, Text
from .block import Block
from .children import Children

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
            "rich_text": [],
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

        Usage
        -----
       >>> from notion_extensions.base.props.block import Callout
       >>> from notion_extensions.base.props.common import Text, Emoji, Icon     
       >>> text = Text("SampleText")
       >>> icon = Icon(Emoji("☺"))
       >>> callout = Callout(text,icon=icon)
        {
            'type': 'callout', 
            'callout': {
                'rich_text': [
                    {
                        'type': 'text', 
                        'text': {'content': 'SampleText', 'link': None}, 
                        'annotations': {
                            'bold': False, 'italic': False, 'strikethrough': False, 
                            'underline': False, 'code': False, 'color': 'default'
                        }
                    }
                ], 
            'icon': {'type': 'emoji', 'emoji': '☺'}
            }

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
        self.__text = RichText(key="rich_text", *base)
        self["callout"].update(self.__text)  # Add Texts with RichText Style
        if children is not None:
            self["callout"].update(children)  # if children exists, Add Chilren

    @property
    def text(self) -> RichText:
        return self.__text

    @text.setter
    def text(self, value: RichText) -> None:
        if value.key != "rich_text":
            raise ValueError("RichText's key is must be `rich_text`")
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
