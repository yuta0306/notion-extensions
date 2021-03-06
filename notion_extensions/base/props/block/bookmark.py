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
