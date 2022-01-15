import sys
from typing import Any, Dict, List, Optional, Union
import warnings

from .common import BaseProps, Text, RichText

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

BLOCK_TYPES = Literal[
    "paragraph",
    "heading_1",
    "heading_2",
    "heading_3",
    "bulleted_list_item",
    "numbered_list_item",
    "to_do",
    "toggle",
    "child_page",
    "child_database",
    "embed",
    "image",
    "video",
    "file",
    "pdf",
    "bookmark",
    "callout",
    "quote",
    "equation",
    "divider",
    "table_of_contents",
    "column",
    "column_list",
    "link_preview",
    "synced_block",
    "template",
    "link_to_page",
    "table",
    "table_row",
    "unsupported",
]


class Paragraph(BaseProps):
    """
    Paragraph
    Paragraph property values of block

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
        "type": "paragraph",
        "paragraph": {
            "text": [
                {
                    "type": "text",
                    "text": {
                        "content": "",
                        "link": None,
                    },
                }
            ],
        },
    }

    def __init__(
        self,
        rich_text: Optional[RichText] = None,
        *text: Text,
    ):
        super().__init__()
        if rich_text is None:
            rich_text = RichText(key="text")
        if rich_text.key != "text":
            raise ValueError("the property key of RichText must be `text`")
        self.__texts = rich_text
        if len(text) > 0:
            self.__texts.extend(list(text))

        self.update(
            {
                "type": "paragraph",
                "paragraph": self.__texts,
            },
        )

    def __add__(self, other: Union[Text, List[Text]]):
        if isinstance(other, list):
            self.extend(other)
            return self
        self.append(other)
        return self

    def __iadd__(self, other: Union[Text, List[Text]]):
        return self.__add__(other)

    def append(self, text: Text) -> None:
        """
        append(text: Text)
            Append Text to existing list of Text

        Parameters
        ----------
        text : Text
            Text you append to RichText
        """
        self.__texts.append(text)
        self["paragraph"] = self.__texts

    def extend(self, texts: List[Text]) -> None:
        """
        extens(texts: Text)
            Append Text to existing list of Text

        Parameters
        ----------
        text : list of Text
            List of text you append to RichText
        """
        self.__texts.extend(texts)
        self["paragraph"] = self.__texts

    def insert(self, index: int, text: Text) -> None:
        """
        insert(index: int, text: Text)
            Append Text to existing list of Text

        Parameters
        ----------
        index : int
            Index you insert Text into
        text : Text
            Text you insert into RichText
        """
        self.__texts.insert(index, text)
        self["paragraph"] = self.__texts

    def pop(self, index=None):
        """
        pop(text: Text)
            Pop Text to existing list of Text

        Parameters
        ----------
        index : int, default=None
            Text you pop from RichText
        """
        item = self.__texts.pop(index)
        self["paragraph"] = self.__texts
        return item
