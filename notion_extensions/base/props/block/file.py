import sys
from typing import Dict, Optional, Union

if sys.version_info >= (3, 8):  # "from typing" in Python 3.9 and earlier
    from typing import Literal
else:
    from typing_extensions import Literal

from .block import Block
from ..common import Text, RichText, FileObject

__all__ = [
    "File",
]


class File(Block):
    """
     File
     File property values of block

    Attributes
    ----------
    url : str
        Link to website the video block will display
    type_ : 'external' or 'file', default='external'
        Type of this file object. Possible values are: 'external', 'file'
    caption : RichText
        Caption of the file block

    Methods
    -------
    clear()
        Clear data of title
    json()
        Return this class as dictionary
    """

    TEMPLATE: Dict[str, Union[str, Dict]] = {
        "type": "file",
        "file": {
            "type": "external",
            "external": {
                "url": "",
            },
        },
    }

    def __init__(
        self,
        *caption: Union[Text, RichText],
        url: Optional[str] = None,
        type_: Literal["external", "file"] = "external",
        file: Optional[FileObject] = None,
    ):
        """
        Parameters
        ----------
        *caption : Text or RichText
            Caption of the file block
        url : str, optional
            Link to website the video block will display
        type_ : 'external' or 'file', default='external'
            Type of this file object. Possible values are: 'external', 'file'
        file : FileObject, optional
            FileObject
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

        if url is None and file is None:
            raise ValueError("Either url or file should be not None")
        elif file is not None:
            self.__file = file
        elif url is not None:
            self.__file = FileObject(type_=type_, url=url)
        self["file"] = self.__file
        self["file"].update(self.__caption)

    @property
    def caption(self) -> RichText:
        return self.__caption

    @caption.setter
    def caption(self, value: RichText) -> None:
        self.__caption = value
        self["file"].update(self.__caption)

    @caption.deleter
    def caption(self) -> None:
        self.__caption = RichText()
        self["file"].update(self.__caption)

    @property
    def type_(self) -> str:
        return self.__file.type_

    @type_.setter
    def type_(self, value: Literal["external", "file"]) -> None:
        self.__file.type_ = value
        self["file"] = self.__file

    @type_.deleter
    def type_(self) -> None:
        self.__file.type_ = "external"
        self["file"] = self.__file

    @property
    def url(self) -> str:
        return self.__file.url

    @url.setter
    def url(self, value: str) -> None:
        self.__file.url = value

    @url.deleter
    def url(self) -> None:
        self.__file.url = ""
