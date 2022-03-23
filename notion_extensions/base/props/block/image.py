import sys
from typing import Dict, List, Optional, Union

if sys.version_info >= (3, 8):  # "from typing" in Python 3.9 and earlier
    from typing import Literal
else:
    from typing_extensions import Literal

from .block import Block
from ..common import Text, RichText, FileObject

__all__ = [
    "Image",
    "IMAGE_EXT",
]

IMAGE_EXT: List[str] = [
    "png",
    "jpg",
    "jpeg",
    "gif",
    "tif",
    "tiff",
    "bmp",
    "svg",
    "heic",
]


class Image(Block):
    """
     Image
     Image property values of block
     Includes supported image urls (i.e. ending in .png, .jpg, .jpeg, .gif, .tif, .tiff, .bmp, .svg, or .heic)

    Attributes
    ----------
    url : str
        Link to website the image block will display
    type_ : 'external' or 'file', default='external'
        Type of this file object. Possible values are: 'external', 'file'

    Methods
    -------
    clear()
        Clear data of title
    json()
        Return this class as dictionary

    Usage
    -----
    >>> from notion_extensions.base.props.block import image
    >>> caption=Text("Sample")
    >>> url=Text("https://www.youtube.com/")
    >>> Image=Text(caption,url)
    >>> Image
    {'type': 'text', 'text': {'content': {'type': 'text', 'text': {'content': 'Sample', 'link': None}, 'annotations': {'bold': False, 'italic': False, 'strikethrough': False, 'underline': False, 'code': False, 'color': 'default'}}, 'link': {'type': 'text', 'text': {'content': 'https://www.youtube.com/', 'link': None}, 'annotations': {'bold': False, 'italic': False, 'strikethrough': False, 'underline': False, 'code': False, 'color': 'default'}}}, 'annotations': {'bold': False, 'italic': False, 'strikethrough': False, 'underline': False, 'code': False, 'color': 'default'}}
    >>>

    """

    TEMPLATE: Dict[str, Union[str, Dict]] = {
        "type": "image",
        "image": {
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
            Caption of the image block
        url : str, optional
            Link to website the image block will display
        type_ : 'external' or 'file', default='external'
            Type of this file object. Possible values are: 'external', 'file'
        file : FileObject, optional
            FileObject

        Usage
        -----






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
            ext = url.split(".")[-1]
            if ext not in IMAGE_EXT:
                raise ValueError(
                    """Includes supported image urls,
                    (i.e. ending in .png, .jpg, .jpeg, .gif, .tif, .tiff, .bmp, .svg, or .heic)"""
                )
            self.__file = FileObject(type_=type_, url=url)
        self["image"] = self.__file
        self["image"].update(self.__caption)

    @property
    def caption(self) -> RichText:
        return self.__caption

    @caption.setter
    def caption(self, value: RichText) -> None:
        self.__caption = value
        self["image"].update(self.__caption)

    @caption.deleter
    def caption(self) -> None:
        self.__caption = RichText()
        self["image"].update(self.__caption)

    @property
    def type_(self) -> str:
        return self.__file.type_

    @type_.setter
    def type_(self, value: Literal["external", "file"]) -> None:
        self.__file.type_ = value
        self["image"] = self.__file

    @type_.deleter
    def type_(self) -> None:
        self.__file.type_ = "external"
        self["image"] = self.__file

    @property
    def url(self) -> str:
        return self.__file.url

    @url.setter
    def url(self, value: str) -> None:
        self.__file.url = value

    @url.deleter
    def url(self) -> None:
        self.__file.url = ""
