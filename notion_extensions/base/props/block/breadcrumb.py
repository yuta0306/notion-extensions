from typing import Dict, Union

from .block import Block

__all__ = [
    "BreadCrumb",
]


class BreadCrumb(Block):
    """
    BreadCrumb
    BreadCrumb property values of block

    Attributes
    ----------

    Methods
    -------
    clear()
        Clear data of title
    json()
        Return this class as dictionary

    Usage
    -----
    >>> from notion_extensions.base.props.block import BreadCrumb
    >>> BreadCrumb()
    {'type': 'breadcrumb', 'breadcrumb': {}}
    """

    TEMPLATE: Dict[str, Union[str, Dict]] = {
        "type": "breadcrumb",
        "breadcrumb": {},
    }

    def __init__(self):
        super().__init__()
