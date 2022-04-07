from typing import Dict, Optional, Union

from ..common import RichText, Text
from .block import Block
from .children import Children

__all__ = [
    "Toggle",
]


class Toggle(Block):
    """
    Toggle
    Toggle property values of block

    Attributes
    ----------
    text : RichText
        Rich text in the toggle block
    children : Children
        Any nested children blocks of the toggle block

    Methods
    -------
    clear()
        Clear data of title
    json()
        Return this class as dictionary
    """

    TEMPLATE: Dict[str, Union[str, Dict, bool]] = {
        "type": "toggle",
        "toggle": {
            "rich_text": [],
            "children": [],
        },
    }

    def __init__(
        self,
        *text: Union[Text, RichText],
        children: Optional[Children] = None,
    ):
        """
        Toggle
        Toggle property values of block

        Parameters
        ----------
        *text : RichText
            Rich text in the toggle block
        children : Children
            Any nested children blocks of the toggle block

        Usage
        -----
        >>> from notion_extensions.base.props.block import Toggle, Children, Paragraph
        >>> from notion_extensions.base.props.common import Text, RichText
        >>> text = Text(text="This is a toggle")
        >>> p1 = Paragraph(Text(text="nested paragraph1"))
        >>> p2 = Paragraph(Text(text="nested paragraph2"))
        >>> children = Children(p1, p2)
        >>> toggle = Toggle(text, children=children)
        >>> toggle
        {
            'type': 'toggle',
            'toggle': {
                'rich_text': [
                    {
                        'type': 'text',
                        'text': {'content': 'This is a toggle', 'link': None},
                        'annotations': {'bold': False, 'italic': False, 'strikethrough': False, 'underline': False,
                                        'code': False, 'color': 'default'}
                    }
                ],
                'children': [
                    {
                        'object': 'block',
                        'type': 'paragraph',
                        'paragraph': {
                            'rich_text': [
                                {
                                    'type': 'text',
                                    'text': {'content': 'nested paragraph1', 'link': None},
                                    'annotations': {'bold': False, 'italic': False, 'strikethrough': False,
                                                    'underline': False, 'code': False, 'color': 'default'}
                                }
                            ]
                        }
                    },
                    {
                        'object': 'block',
                        'type': 'paragraph',
                        'paragraph': {
                            'rich_text': [
                                {
                                    'type': 'text',
                                    'text': {'content': 'nested paragraph2', 'link': None},
                                    'annotations': {'bold': False, 'italic': False, 'strikethrough': False,
                                                    'underline': False, 'code': False, 'color': 'default'}
                                }
                            ]
                        }
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
        self["toggle"].update(self.__text)  # Add Texts with RichText Style
        if children is not None:
            self["toggle"].update(children)  # if children exists, Add Chilren

    @property
    def text(self) -> RichText:
        return self.__text

    @text.setter
    def text(self, value: RichText) -> None:
        if value.key != "text":
            raise ValueError("RichText's key is must be `text`")
        self.__text = value
        self["toggle"].update(self.__text)

    @property
    def children(self) -> Children:
        return self["toggle"]["children"]

    @children.setter
    def children(self, value: Children) -> None:
        self["toggle"].update(value)
