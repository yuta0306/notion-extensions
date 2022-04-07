import sys
from typing import Dict, Optional, Union

if sys.version_info >= (3, 8):  # "from typing" in Python 3.9 and earlier
    from typing import Literal
else:
    from typing_extensions import Literal

from ..common import FileObject, RichText, Text
from .block import Block

__all__ = [
    "Video",
]


class Video(Block):
    """
    Video
    Video property values of block

    Attributes
    ----------
    caption : RichText
            Caption of the video block
    url : str
        Link to website the video block will display
    type_ : 'external' or 'file', default='external'
        Type of this file object. Possible values are: 'external', 'file'

    Methods
    -------
    clear()
        Clear data of title
    json()
        Return this class as dictionary
    """

    TEMPLATE: Dict[str, Union[str, Dict]] = {
        "type": "video",
        "video": {
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
        Video
        Video property values of block

        Parameters
        ----------
        *caption : Text or RichText
            Caption of the video block
        url : str, optional
            Link to website the video block will display
        type_ : 'external' or 'file', default='external'
            Type of this file object. Possible values are: 'external', 'file'
        file : FileObject, optional
            FileObject

        Raises
        ------
        ValueError
            The set of Text or RichText are not given as caption
        ValueError
            url and file are given as None

        Usage
        -----
        >>> from notion_extensions.base.props.block import Video
        >>> from notion_extensions.base.props.common import Text, RichText, FileObject
        >>> url = "https://..."
        >>> text = Text("This is a caption")
        >>> video = Video(text, url=url, type_="external")
        >>> video
        {
            'type': 'video',
            'video': {
                'type': 'external',
                'external': {'url': 'https://...'},
                'caption': [
                    {
                        'type': 'text',
                        'text': {'content': 'This is a caption', 'link': None},
                        'annotations': {'bold': False, 'italic': False, 'strikethrough': False,
                                        'underline': False, 'code': False, 'color': 'default'}
                    }
                ]
            }
        }
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
        self["video"] = self.__file
        self["video"].update(self.__caption)

    @property
    def caption(self) -> RichText:
        return self.__caption

    @caption.setter
    def caption(self, value: RichText) -> None:
        self.__caption = value
        self["video"].update(self.__caption)

    @caption.deleter
    def caption(self) -> None:
        self.__caption = RichText()
        self["video"].update(self.__caption)

    @property
    def type_(self) -> str:
        return self.__file.type_

    @type_.setter
    def type_(self, value: Literal["external", "file"]) -> None:
        self.__file.type_ = value
        self["video"] = self.__file

    @type_.deleter
    def type_(self) -> None:
        self.__file.type_ = "external"
        self["video"] = self.__file

    @property
    def url(self) -> str:
        return self.__file.url

    @url.setter
    def url(self, value: str) -> None:
        self.__file.url = value

    @url.deleter
    def url(self) -> None:
        self.__file.url = ""
