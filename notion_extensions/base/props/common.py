import copy
from typing import Any, Dict, List, Optional, Union
import warnings


class BaseProps(dict):
    TEMPLATE: Dict = {}

    def __init__(self):
        super().__init__()
        self.update(self.TEMPLATE)

    def __setitem__(self, key: Any, item: Any):
        item = copy.deepcopy(item)
        super().__setitem__(key, item)

    def __delitem__(self, key):
        """
        Raises
        ------
        NotImplementedError
        """
        raise NotImplementedError

    def json(self) -> dict:
        warnings.warn("deprecated", FutureWarning)
        json = super().copy()
        return json

    def pop(self):
        """
        pop()

        Raises
        ------
        NotImplementedError
        """
        raise NotImplementedError

    def popitem(self):
        """
        popitem()

        Raises
        ------
        NotImplementedError
        """
        raise NotImplementedError

    def clear(self) -> None:
        """
        clear()

        Returns
        -------
        None
        """
        self.update(self.TEMPLATE)

    def update(self, __mapping, **kwargs):
        """
        update(__mapping: Dict[Any, Any], **kwargs)

        Returns
        -------
        None
        """
        for key, value in __mapping.items():
            self.__setitem__(key, value)

    def setdefault(self, __key, __default):
        """
        Raises
        ------
        NotImplementedError
        """
        raise NotImplementedError


class Annotations(BaseProps):
    """
    Annotations
    Text property values of a common structure

    Attributes
    ----------
    bold : bool, default=False
        bold text
    italic : bool, default=False
        italic text
    strikethrough : bool, default=False
        strikethrough text
    underline : bool, default=False
        underline text
    code : bool, default=False
        code text
    color : str, default='default'
        text color

    Methods
    -------
    clear()
        Clear data of text
    """

    TEMPLATE: Dict[str, Dict[str, Union[str, bool]]] = {
        "annotations": {
            "bold": False,
            "italic": False,
            "strikethrough": False,
            "underline": False,
            "code": False,
            "color": "default",
        },
    }

    def __init__(
        self,
        bold: bool = False,
        italic: bool = False,
        strikethrough: bool = False,
        underline: bool = False,
        code: bool = False,
        color: str = "default",
    ):
        super().__init__()
        self.bold = bold
        self.italic = italic
        self.strikethrough = strikethrough
        self.underline = underline
        self.code = code
        self.color = color

    @property
    def bold(self):
        return self["annotations"]["bold"]

    @bold.setter
    def bold(self, value: bool):
        self["annotations"]["bold"] = value

    @bold.deleter
    def bold(self) -> None:
        self["annotations"]["bold"] = False

    @property
    def italic(self):
        return self["annotations"]["italic"]

    @italic.setter
    def italic(self, value: bool):
        self["annotations"]["italic"] = value

    @italic.deleter
    def italic(self) -> None:
        self["annotations"]["italic"] = False

    @property
    def strikethrough(self):
        return self["annotations"]["strikethrough"]

    @strikethrough.setter
    def strikethrough(self, value: bool):
        self["annotations"]["strikethrough"] = value

    @strikethrough.deleter
    def strikethrough(self) -> None:
        self["annotations"]["strikethrough"] = False

    @property
    def underline(self):
        return self["annotations"]["underline"]

    @underline.setter
    def underline(self, value: bool):
        self["annotations"]["underline"] = value

    @underline.deleter
    def underline(self) -> None:
        self["annotations"]["underline"] = False

    @property
    def code(self):
        return self["annotations"]["code"]

    @code.setter
    def code(self, value: bool):
        self["annotations"]["code"] = value

    @code.deleter
    def code(self) -> None:
        self["annotations"]["code"] = False

    @property
    def color(self):
        return self["annotations"]["color"]

    @color.setter
    def color(self, value: str):
        self["annotations"]["color"] = value

    @color.deleter
    def color(self) -> None:
        self["annotations"]["color"] = "default"


class PlainText(BaseProps):
    """
    PlainText
    Text property values, this is a plain text and does not have any text decoration

    Attributes
    ----------
    text : str
        Text

    Methods
    -------
    clear()
        Clear data of text
    """

    TEMPLATE: Dict[str, Union[str, Dict]] = {
        "type": "text",
        "text": {
            "content": "",
        },
    }

    def __init__(self, text: str = ""):
        super().__init__()
        self.text = text

    def __add__(self, other: str):
        self.text = self.text + other
        return self

    def __iadd__(self, other: str):
        return self.__add__(other)

    @property
    def text(self) -> str:
        return self["text"]["content"]

    @text.setter
    def text(self, value: str) -> None:
        self["text"]["content"] = value

    @text.deleter
    def text(self) -> None:
        self["text"]["content"] = ""


class Text(BaseProps):
    """
    Text
    Text property values

    Attributes
    ----------
    text: str, default=''
        text
    bold : bool, default=False
        bold text
    italic : bool, default=False
        italic text
    strikethrough : bool, default=False
        strikethrough text
    underline : bool, default=False
        underline text
    code : bool, default=False
        code text
    color : str, default='default'
        text color

    Methods
    -------
    clear()
        Clear data of text
    """

    TEMPLATE: Dict[str, Union[str, Dict[str, Union[str, bool]]]] = {
        "type": "text",
        "text": {
            "content": "",
        },
        "annotations": {
            "bold": False,
            "italic": False,
            "strikethrough": False,
            "underline": False,
            "code": False,
            "color": "default",
        },
    }

    def __init__(
        self,
        text: str = "",
        bold: bool = False,
        italic: bool = False,
        strikethrough: bool = False,
        underline: bool = False,
        code: bool = False,
        color: str = "default",
    ):
        super().__init__()
        self.__text = PlainText(text=text)
        self.__annotations = Annotations(
            bold=bold,
            italic=italic,
            strikethrough=strikethrough,
            underline=underline,
            code=code,
            color=color,
        )
        self.update(self.__text)
        self.update(self.__annotations)

    @property
    def text(self):
        return self.__text.text

    @text.setter
    def text(self, value: str):
        self.__text.text = value

    @text.deleter
    def text(self):
        del self.__text.text

    @property
    def bold(self):
        return self.__annotations.bold

    @bold.setter
    def bold(self, value: bool):
        self.__annotations.bold = value

    @bold.deleter
    def bold(self) -> None:
        del self.__annotations.bold

    @property
    def italic(self):
        return self.__annotations.italic

    @italic.setter
    def italic(self, value: bool):
        self.__annotations.italic = value

    @italic.deleter
    def italic(self) -> None:
        del self.__annotations.italic

    @property
    def strikethrough(self):
        return self.__annotations.strikethrough

    @strikethrough.setter
    def strikethrough(self, value: bool):
        self.__annotations.strikethrough = value

    @strikethrough.deleter
    def strikethrough(self) -> None:
        del self.__annotations.strikethrough

    @property
    def underline(self):
        return self.__annotations.underline

    @underline.setter
    def underline(self, value: bool):
        self.__annotations.underline = value

    @underline.deleter
    def underline(self) -> None:
        del self.__annotations.underline

    @property
    def code(self):
        return self.__annotations.code

    @code.setter
    def code(self, value: bool):
        self.__annotations.code = value

    @code.deleter
    def code(self) -> None:
        del self.__annotations.code

    @property
    def color(self):
        return self.__annotations.color

    @color.setter
    def color(self, value: str):
        self.__annotations.color = value

    @color.deleter
    def color(self):
        del self.__annotations.color


class RichText(BaseProps):
    """
    RichText
    RichText property values

    Methods
    -------
    append(text: Text)
        Append Text to existing list of Text
    extend(texts: List[Text])
        Extend list of Text to existing list of Text
    insert(index: int, Text)
        Insert Text into specific index of existing list of Text
    pop(index: int=None)
        Pop Text from specific index of existing list of Text
    clear()
        Clear data of text
    """

    TEMPLATE: Dict[str, List[Text]] = {
        "rich_text": [],
    }

    def __init__(
        self,
        *text: Text,
        key: str = "rich_text",
    ):
        """
        Parameters
        ----------
        key : str
            Property key of RichText
        *text: Text
            Texts of RichText
        """
        super().__init__()
        self.__key = key
        self.__texts = list(text)
        self.update(
            {
                key: self.__texts,
            }
        )
        if key != "rich_text":
            super(BaseProps, self).pop("rich_text")

    def __getitem__(self, index: Union[int, str]) -> Text:
        if isinstance(index, int):
            return self.__texts[index]
        return super().__getitem__(index)

    def __add__(self, other: Union[Text, List[Text]]):
        if isinstance(other, list):
            self.extend(other)
            return self
        self.append(other)
        return self

    def __iadd__(self, other: Union[Text, List[Text]]):
        return self.__add__(other)

    @property
    def key(self) -> str:
        return self.__key

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
        self[self.key] = self.__texts

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
        self[self.key] = self.__texts

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
        self[self.key] = self.__texts

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
        self[self.key] = self.__texts
        return item


class Emoji(BaseProps):
    """
    Emoji
    Emoji property values

    Attributes
    ----------
    emoji : str
        Emoji

    Methods
    -------
    clear()
        Clear data of emoji
    """

    TEMPLATE: Dict[str, str] = {
        "type": "emoji",
        "emoji": "",
    }

    def __init__(self, emoji: str):
        """
        Parameters
        ----------
        emoji : str
            Emoji
        """
        super().__init__()
        self["emoji"] = emoji

    @property
    def emoji(self) -> str:
        return self["emoji"]

    @emoji.setter
    def emoji(self, value: str) -> None:
        self["emoji"] = value

    @emoji.deleter
    def emoji(self) -> None:
        self["emoji"] = ""


class File(BaseProps):
    def __init__(self):
        super().__init__()
        raise NotImplementedError


class Icon(BaseProps):
    """
    Icon
    Icon property values

    Attributes
    ----------
    emoji : Emoji
        Emoji Object

    Methods
    -------
    clear()
        Clear data of emoji

    .. note:: file object is not be implemented yet
    """

    TEMPLATE: Dict[str, Dict] = {
        "icon": {},
    }

    def __init__(self, emoji: Emoji, file: Optional[File] = None):
        """
        Parameters
        ----------
        emoji : Emoji
            Emoji Object
        file : File, optional
            File Object

        .. note:: file object is not be implemented yet
        """
        super().__init__()
        self["icon"] = emoji

    @property
    def emoji(self) -> Emoji:
        return self["icon"]

    @emoji.setter
    def emoji(self, value: Emoji) -> None:
        self["icon"] = value

    @emoji.deleter
    def emoji(self) -> None:
        self["icon"] = {}
