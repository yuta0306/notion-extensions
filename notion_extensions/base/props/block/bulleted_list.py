from typing import Dict, Optional, Union

from ..common import RichText, Text
from .block import Block
from .children import Children

__all__ = [
    "BulletedListItem",
    "BulletedList",
]


class BulletedListItem(Block):
    """
    BulletedListItem
    BulletedListItem property values of block

    Attributes
    ----------
    *text : Text or RichText
        text
    children : Children, optional
        children

    Methods
    -------
    clear()
        Clear data of title
    json()
        Return this class as dictionary
    """

    TEMPLATE: Dict[str, Union[str, Dict]] = {
        "type": "bulleted_list_item",
        "bulleted_list_item": {
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

        Usage
        -----
        >>> from notion_extensions.base.props.block import BulletedListItem
        >>> text = Text("text")
        >>> bulleted_list_item = BulletedListItem(text)
        >>> bulleted_list_item
        {
            'type': 'bulleted_list_item',
                'bulleted_list_item': {
                    'text': [
                        {
                            'type': 'text',
                            'text': {'content': 'text', 'link': None},
                            'annotations': {'bold': False, 'italic': False, 'strikethrough': False,
                            'underline': False, 'code': False, 'color': 'default'}
                        }
                    ]
                }
        }
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
        self["bulleted_list_item"].update(self.__text)  # Add Texts with RichText Style
        if children is not None:
            self["bulleted_list_item"].update(
                children
            )  # if children exists, Add Chilren

    @property
    def text(self) -> RichText:
        return self.__text

    @text.setter
    def text(self, value: RichText) -> None:
        if value.key != "rich_text":
            raise ValueError("RichText's key is must be `rich_text`")
        self.__text = value
        self["bulleted_list_item"].update(self.__text)

    @property
    def children(self) -> Children:
        return self["bulleted_list_item"]["children"]

    @children.setter
    def children(self, value: Children) -> None:
        self["bulleted_list_item"].update(value)


class BulletedList(Children):
    """
    BulletedList
    BulletedList property values of block

    Attributes
    ----------

    Methods
    -------
    clear()
        Clear data of title
    json()
        Return this class as dictionary
    """

    def __init__(
        self,
        *item: BulletedListItem,
    ):
        """
        Parameters
        ----------
        *item : BulletedListItem
            items of bulleted list item
        """
        super().__init__(*item)
