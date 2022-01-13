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

    def __setitem__(self, key: str, item: Any) -> NoReturn:
        return super().__setitem__(key, item)

    def __delitem__(self, key) -> NoReturn:
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
        self['bold'] = bold
        self['italic'] = italic
        self['strikethrough'] = strikethrough
        self['underline'] = underline
        self['code'] = code
        self['color'] = color

    @property
    def bold(self):
        return self.data['annotations']['bold']

    @bold.setter
    def bold(self, value: bool):
        self['bold'] = value

    @bold.deleter
    def bold(self) -> NoReturn:
        self['bold'] = False

    @property
    def italic(self):
        return self.data['annotations']['italic']

    @italic.setter
    def italic(self, value: bool):
        self['italic'] = value

    @italic.deleter
    def italic(self) -> NoReturn:
        self['italic'] = False

    @property
    def strikethrough(self):
        return self.data['annotations']['strikethrough']

    @strikethrough.setter
    def strikethrough(self, value: bool):
        self['strikethrough'] = value

    @strikethrough.deleter
    def strikethrough(self) -> NoReturn:
        self['strikethrough'] = False

    @property
    def underline(self):
        return self.data['annotations']['underline']

    @underline.setter
    def underline(self, value: bool):
        self['underline'] = value

    @underline.deleter
    def underline(self) -> NoReturn:
        self['underline'] = False

    @property
    def code(self):
        return self.data['annotations']['code']

    @code.setter
    def code(self, value: bool):
        self['code'] = value

    @code.deleter
    def code(self) -> NoReturn:
        self['code'] = False

    @property
    def color(self):
        return self.data['annotations']['color']

    @color.setter
    def color(self, value: str):
        self['color'] = value

    @color.deleter
    def color(self) -> NoReturn:
        self['color'] = 'default'

    def __setitem__(self, key: Literal['bold', 'italic', 'strikethrough', 'underline', 'code', 'color'],
                    item: Union[bool, str]) -> NoReturn:
        if key not in ('bold', 'italic', 'strikethrough', 'underline', 'code', 'color'):
            raise KeyError(f'key must be `bold`or `italic`or `strikethrough`or `underline`or `code`or `color`, but {key}')
        self.data['annotations'][key] = item


class Text(BaseProps):
    """
    Text
    Text property values of a common structure

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
        self.__text = text
        self.data['text'] = text

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, value: str):
        self.__text = value
        self['text'] = value

    @text.deleter
    def text(self) -> NoReturn:
        self.__text = ''
        self['text'] = ''

    def __setitem__(self, key: Literal['text', 'content'], item: str) -> NoReturn:
        if key not in ('text', 'content'):
            raise KeyError(f'key must be `text` or `content`, but {key}')
        self.__text = item
        self.data['text']['content'] = item