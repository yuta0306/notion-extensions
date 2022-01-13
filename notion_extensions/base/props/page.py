from collections import UserDict
from typing import Any, Dict, Final, List, NoReturn, Tuple, Union, Optional
try:
    from typing import Literal
except:
    from typing_extensions import Literal

from .common import BaseProps, PlainText

class Title(BaseProps):
    """
    Title
    Title property values of a page

    rich_text cannot be used because it's not implemented

    Attributes
    ----------
    title : str
        Title of a page
    id_ : str, default='title'
        Title property ID
    in_page : bool, default=True
        Page is created in page or not. If page is not in page, page is in database
        if in_page is True, ID is set to `title`.

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
    def __init__(self, title: str = '', id_: str = 'title', in_page: bool = True):
        """
        Parameters
        ----------
        title : str, default=''
            Title of a page
        id_ : str, default='title'
            Title property ID
        in_page : bool, default=True
            Page is created in page or not. If page is not in page, page is in database
            if in_page is True, ID is set to `title`.
        """
        super().__init__()
        self.__title = PlainText(text=title)
        self.id_ = id_
        self.in_page = in_page

    @property
    def data(self):
        id_ = self.id_ if not self.in_page else 'title'
        return {
            id_: {
                'title': [
                    self.__title.json(),
                ],
            },
        }
    
    @data.setter
    def data(self, value):
        pass

    @property
    def title(self) -> str:
        """
        Title of a page
        """
        return self.__title.text

    @title.setter
    def title(self, value: str) -> NoReturn:
        self.__title.text = value

    @title.deleter
    def title(self) -> NoReturn:
        del self.__title.text
