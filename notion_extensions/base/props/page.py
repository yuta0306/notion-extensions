from collections import UserDict
from typing import Any, Dict, Final, List, NoReturn, Tuple, Union, Optional
try:
    from typing import Literal
except:
    from typing_extensions import Literal

from .common import BaseProps

class Title(BaseProps):
    """
    Title
    Title property values of a page

    rich_text cannot be used because it's not implemented

    Attributes
    ----------
    title : str
        Title of a page

    Methods
    -------
    clear()
        Clear data of title
    json()
        Return this class as dictionary
    """
    TEMPLATE: Final[Dict] = {
        'title': [
            {
                'type': 'text',
                'text': {
                    'content': '',
                },
            },
        ],
    }
    def __init__(self, title: str = ''):
        """
        Parameters
        ----------
        title : str, default=''
            Title of a page
        """
        super().__init__()
        self['content'] = title
        self.__title = title

    @property
    def title(self) -> str:
        """
        Title of a page
        """
        return self.__title

    @title.setter
    def title(self, value: str) -> NoReturn:
        self.__title = str(value)
        self['content'] = str(value)

    @title.deleter
    def title(self) -> NoReturn:
        self.__title = ''
        self['content'] = ''

    def __setitem__(self, key: Literal['content', 'title'], item: str) -> NoReturn:
        if key not in ('content', 'title'):
            raise KeyError(f'key must be `content` or `title`, but {key}')
        item = str(item)
        self.data['title'][0]['text']['content'] = item
        self.__title = item
