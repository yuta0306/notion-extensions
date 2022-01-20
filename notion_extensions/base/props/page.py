import sys
from typing import Dict, List, Optional, Text
import warnings

if sys.version_info > (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

from .common import BaseProps, PlainText

__all__ = [
    "Title",
    "Parent",
]


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

    TEMPLATE: Dict[str, List[Text]] = {
        "title": [],
    }

    def __init__(self, title: str = "", id_: str = "title", in_page: bool = True):
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
        self.__title: PlainText = PlainText(text=title)
        self.__id: str = id_
        self.__in_page: bool = in_page
        if in_page:  # create page in page
            self.update(
                {
                    "title": {
                        "title": [self.__title],
                    },
                }
            )
        else:  # create page in database
            self.update(
                {
                    id_: {
                        "title": [self.__title],
                    },
                }
            )

    @property
    def title(self) -> str:
        """
        Title of a page
        """
        return self.__title.text

    @title.setter
    def title(self, value: str) -> None:
        self.__title.text = value

    @title.deleter
    def title(self) -> None:
        del self.__title.text

    @property
    def id_(self):
        return self.__id

    @id_.setter
    def id_(self, value: str) -> None:
        if self.__in_page:
            if value == "title":
                self.__id = value
            else:
                warnings.warn(
                    "If you create page in page, id_ must be `title`", UserWarning
                )
        else:
            self.__id = value

    @id_.deleter
    def id_(self):
        self.__id = "title"

    @property
    def in_page(self) -> bool:
        return self.__in_page

    @in_page.setter
    def in_page(self, value: bool) -> None:
        self.__in_page = value
        if value:
            self.__id = "title"

    @in_page.deleter
    def in_page(self):
        self.__in_page = True


class Parent(BaseProps):
    """
    Parent
    Parent property values of a page

    Attributes
    ----------
    parent_type : 'page' or 'database' or 'workspace'
        The parent of this page. Can be a database, page, or workspace
    id_ : str
        The ID of the page, database or workspace that this page belongs to

    Methods
    -------
    clear()
        Clear data of title
    json()
        Return this class as dictionary
    """

    TEMPLATE: Dict[str, str] = {}

    def __init__(
        self,
        parent_type: Literal["page", "database", "workspace"],
        id_: Optional[str] = None,
    ):
        super().__init__()
        if parent_type in ("page", "database"):
            if id_ is None:
                raise ValueError()
        self["type"] = f"{parent_type}_id"
        if parent_type in ("workspace",):
            self[parent_type] = True
        else:
            self[f"{parent_type}_id"] = id_

    @property
    def parent_type(self):
        return self["type"]

    @property
    def id_(self):
        return self[self.parent_type]
