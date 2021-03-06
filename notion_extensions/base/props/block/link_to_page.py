import sys
from typing import Dict, Union

if sys.version_info >= (3, 8):  # "from typing" in Python 3.9 and earlier
    from typing import Literal
else:
    from typing_extensions import Literal

from .block import Block
from ...utils import parse_id

__all__ = [
    "LinkToPage",
]


class LinkToPage(Block):
    """
     LinkToPage
     LinkToPage property values of block

    Attributes
    ----------
    type_ : str
        Type of this link to page object. Possible values are: "page", "database"
    id_ : str
        Identifier for a page or a database page

    Methods
    -------
    clear()
        Clear data of title
    json()
        Return this class as dictionary
    """

    TEMPLATE: Dict[str, Union[str, Dict]] = {
        "type": "link_to_page",
        "link_to_page": {},
    }

    def __init__(
        self,
        type_: Literal["page", "database"],
        id_: str,
    ):
        """
        Parameters
        ----------
        type_ : 'page' or 'database'
            Type of this link to page object. Possible values are: "page", "database"
        id_ : str
            Identifier for a page or a database page, URL style is ok.
        """
        super().__init__()
        if type_ not in ("page", "database"):
            raise ValueError("type_ must be `page` or `database`")
        id_ = parse_id(id_=id_, type_=type_)
        type_ = f"{type_}_id"
        self["link_to_page"]["type"] = type_
        self["link_to_page"][type_] = id_

    @property
    def type_(self) -> str:
        return self["link_to_page"]["type"]

    @property
    def id_(self) -> str:
        return self["link_to_page"][self.type_]
