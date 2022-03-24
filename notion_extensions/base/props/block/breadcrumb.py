from typing import Dict, Union

from .block import Block

__all__ = [
    "BreadCrumb",
]


class BreadCrumb(Block):
    """
    BreadCrumb
    BreadCrumb property values of block

    Methods
    -------
    clear()
        Clear data of title
    json()
        Return this class as dictionary  
    """

    TEMPLATE: Dict[str, Union[str, Dict]] = {
        "type": "breadcrumb",
        "breadcrumb": {},
    }

    def __init__(self):
        """
        BreadCrumb
        BreadCrumb property values of block
        
        Usage
        -----
        >>> from notion_extensions.base.props.block import BreadCrumb
        >>> bread_crumb=BreadCrumb()
        >>> bread_crumb
        {'type': 'breadcrumb', 'breadcrumb': {}}
        """
        super().__init__()
        