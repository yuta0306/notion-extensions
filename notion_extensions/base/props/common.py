from collections import UserDict
from typing import Any, Dict, Final, List, NoReturn, Tuple, Union, Optional
try:
    from typing import Literal
except:
    from typing_extensions import Literal

class BaseProps(UserDict):
    TEMPLATE: Dict = {}
    def __init__(self):
        super().__init__()
        self.data = self.TEMPLATE

    def __setitem__(self, key: str, item: Any):
        """
        Raises
        ------
        NotImplementedError
        """
        raise NotImplementedError

    def __delitem__(self, key):
        """
        Raises
        ------
        NotImplementedError
        """
        raise NotImplementedError

    def json(self) -> dict:
        return self.data.copy()

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

    def clear(self) -> NoReturn:
        """
        clear()

        Returns
        -------
        NoReturn
        """
        self.data = self.TEMPLATE

    def update(self) -> NoReturn:
        """
        Raises
        ------
        NotImplementedError
        """
        raise NotImplementedError

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
    json()
        Return this class as dictionary
    """
    TEMPLATE: Final[Dict] = {
        "annotations": {
            "bold": False,
            "italic": False,
            "strikethrough": False,
            "underline": False,
            "code": False,
            "color": "default",
        },
    }
    def __init__(self, bold: bool = False, italic: bool = False, strikethrough: bool = False,
                 underline: bool = False, code: bool = False, color: str = 'default'):
        super().__init__()
        self.bold = bold
        self.italic = italic
        self.strikethrough = strikethrough
        self.underline = underline
        self.code = code
        self.color = color

    @property
    def bold(self):
        return self.data['annotations']['bold']

    @bold.setter
    def bold(self, value: bool):
        self.data['annotations']['bold'] = value

    @bold.deleter
    def bold(self) -> NoReturn:
        self.data['annotations']['bold'] = False

    @property
    def italic(self):
        return self.data['annotations']['italic']

    @italic.setter
    def italic(self, value: bool):
        self.data['annotations']['italic'] = value

    @italic.deleter
    def italic(self) -> NoReturn:
        self.data['annotations']['italic'] = False

    @property
    def strikethrough(self):
        return self.data['annotations']['strikethrough']

    @strikethrough.setter
    def strikethrough(self, value: bool):
        self.data['annotations']['strikethrough'] = value

    @strikethrough.deleter
    def strikethrough(self) -> NoReturn:
        self.data['annotations']['strikethrough'] = False

    @property
    def underline(self):
        return self.data['annotations']['underline']

    @underline.setter
    def underline(self, value: bool):
        self.data['annotations']['underline'] = value

    @underline.deleter
    def underline(self) -> NoReturn:
        self.data['annotations']['underline'] = False

    @property
    def code(self):
        return self.data['annotations']['code']

    @code.setter
    def code(self, value: bool):
        self.data['annotations']['code'] = value

    @code.deleter
    def code(self) -> NoReturn:
        self.data['annotations']['code'] = False

    @property
    def color(self):
        return self.data['annotations']['color']

    @color.setter
    def color(self, value: str):
        self.data['annotations']['color'] = value

    @color.deleter
    def color(self) -> NoReturn:
        self.data['annotations']['color'] = 'default'

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
    json()
        Return this class as dictionary
    """
    TEMPLATE: Final[Dict] = {
        "type": "text",
        "text": {
            "content": "The title",
        },
    }
    def __init__(self, text: str = ''):
        super().__init__()
        self.text = text

    @property
    def text(self):
        return self.data['text']['content']

    @text.setter
    def text(self, value: str):
        self.data['text']['content'] = value

    @text.deleter
    def text(self) -> NoReturn:
        self.data['text']['content'] = ''

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
    json()
        Return this class as dictionary
    """
    TEMPLATE: Final[Dict] = {
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
    def __init__(self, text: str = '', bold: bool = False, italic: bool = False, strikethrough: bool = False,
                 underline: bool = False, code: bool = False, color: str = 'default'):
        super().__init__()
        self.__text = PlainText(text=text)
        self.__annotations = Annotations(bold=bold, italic=italic, strikethrough=strikethrough,
                                         underline=underline, code=code, color=color)

    @property
    def data(self):
        pairs = [
            *self.__text.items(),
            *self.__annotations.items()
        ]
        return dict(pairs)

    @data.setter
    def data(self, value):
        pass

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
    def bold(self) -> NoReturn:
        del self.__annotations.bold

    @property
    def italic(self):
        return self.__annotations.italic

    @italic.setter
    def italic(self, value: bool):
        self.__annotations.italic = value

    @italic.deleter
    def italic(self) -> NoReturn:
        del self.__annotations.italic

    @property
    def strikethrough(self):
        return self.__annotations.strikethrough

    @strikethrough.setter
    def strikethrough(self, value: bool):
        self.__annotations.strikethrough = value

    @strikethrough.deleter
    def strikethrough(self) -> NoReturn:
        del self.__annotations.strikethrough

    @property
    def underline(self):
        return self.__annotations.underline

    @underline.setter
    def underline(self, value: bool):
        self.__annotations.underline = value

    @underline.deleter
    def underline(self) -> NoReturn:
        del self.__annotations.underline

    @property
    def code(self):
        return self.__annotations.code

    @code.setter
    def code(self, value: bool):
        self.__annotations.code = value

    @code.deleter
    def code(self) -> NoReturn:
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