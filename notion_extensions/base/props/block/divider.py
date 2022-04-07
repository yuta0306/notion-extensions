from typing import Dict, Union

from .block import Block

__all__ = [
    "Divider",
]


class Divider(Block):
    """
    Divider
    Divider property values of block

    Attributes
    ----------

    Methods
    -------
    clear()
        Clear data of title
    json()
        Return this class as dictionary
    """

    TEMPLATE: Dict[str, Union[str, Dict]] = {
        "type": "divider",
        "divider": {},
    }

    def __init__(self):
        """
        Usage
        -----
        >>> from notion_extensions.base.props.block import Divider
        >>> divider = Divider()
        >>> divider
        {'type': 'divider', 'divider': {}}
        """
        super().__init__()
