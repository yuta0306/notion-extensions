from typing import Dict, Union

from .block import Block
from ..common import Text, RichText

__all__ = [
    "Bookmark",
]


class Bookmark(Block):
    """
     Bookmark
     Bookmark property values of block

    Attributes
    ----------
    url : str
        Link to website the Bookmark block will display
    caption : RichText
        Caption of the pdf block

    Methods
    -------
    clear()
        Clear data of title
    json()
        Return this class as dictionary
    
    Usage
    ------
    >>> from notion_extensions.base.props.common.common import Text
    >>> from notion_extensions.base.props.common import RichText
    >>> from notion_extensions.base.props.block.paragraph import *
    >>> text1 = Text("R",color="red") 
    >>> text2 = Text("G",color="green")
    >>> richText = RichText(text1,text2)       
    >>> richText
    >>> url=Text("https:...")
    >>> caption=richText
    >>> Bookmark=Text(url,caption)  
    >>> Bookmark
    {'type': 'text', 'text': {'content': {'type': 'text', 'text': {'content': 'https://www.notion.so/0ed6cb478e6f40bc9a9408f4f0d084a8', 'link': None}, 'annotations': {'bold': False, 'italic': False, 'strikethrough': False, 'underline': False, 'code': False, 'color': 'default'}}, 'link': {'rich_text': [{'type': 'text', 'text': {'content': 'R', 'link': None}, 'annotations': {'bold': False, 'italic': False, 'strikethrough': False, 'underline': False, 'code': False, 'color': 'red'}}, {'type': 'text', 'text': {'content': 'G', 'link': None}, 'annotations': {'bold': False, 'italic': False, 'strikethrough': False, 'underline': False, 'code': False, 'color': 'green'}}]}}, 'annotations': {'bold': False, 'italic': False, 'strikethrough': False, 'underline': False, 'code': False, 'color': 'default'}}

    """

    TEMPLATE: Dict[str, Union[str, Dict]] = {
        "type": "bookmark",
        "bookmark": {
            "url": "",
        },
    }

    def __init__(
        self,
        url: str,
        *caption: Union[Text, RichText],
    ):
        """
        Parameters
        ----------
        url : str
            Link to website the bookmark block will display
        *caption : Text or RichText
            Caption of the bookmark block
        """
        super().__init__()
        base = []  # Aggregate Texts
        for t in caption:
            if isinstance(t, RichText):
                base.extend(list(t[t.key]))
            elif isinstance(t, Text):
                base.append(t)
            else:
                raise ValueError(
                    f"Expected type is `RichText` or `Text`, but {type(t)} is given"
                )
        self.__caption = RichText(key="caption", *base)
        self["bookmark"]["url"] = url
        self["bookmark"].update(self.__caption)

    @property
    def caption(self) -> RichText:
        return self.__caption

    @caption.setter
    def caption(self, value: RichText) -> None:
        self.__caption = value
        self["bookmark"].update(self.__caption)

    @caption.deleter
    def caption(self) -> None:
        self.__caption = RichText()
        self["bookmark"].update(self.__caption)

    @property
    def url(self) -> str:
        return self["bookmark"]["url"]

    @url.setter
    def url(self, value: str) -> None:
        self["bookmark"]["url"] = value

    @url.deleter
    def url(self) -> None:
        self["bookmark"]["url"] = ""
