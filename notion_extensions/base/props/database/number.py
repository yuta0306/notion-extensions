import sys

if sys.version_info > (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

from ..common import BaseProps

__all__ = [
    "AVAILABLE_FORMAT",
    "Number",
]

AVAILABLE_FORMAT = [
    "number",
    "number_with_commas",
    "percent",
    "dollar",
    "canadian_dollar",
    "euro",
    "pound",
    "yen",
    "ruble",
    "rupee",
    "won",
    "yuan",
    "real",
    "lira",
    "rupiah",
    "franc",
    "hong_kong_dollar",
    "new_zealand_dollar",
    "krona",
    "norwegian_krone",
    "mexican_peso",
    "rand",
    "new_taiwan_dollar",
    "danish_krone",
    "zloty",
    "baht",
    "forint",
    "koruna",
    "shekel",
    "chilean_peso",
    "philippine_peso",
    "dirham",
    "colombian_peso",
    "riyal",
    "ringgit",
    "leu",
]

FORMAT: TypeAlias = Literal[
    "number",
    "number_with_commas",
    "percent",
    "dollar",
    "canadian_dollar",
    "euro",
    "pound",
    "yen",
    "ruble",
    "rupee",
    "won",
    "yuan",
    "real",
    "lira",
    "rupiah",
    "franc",
    "hong_kong_dollar",
    "new_zealand_dollar",
    "krona",
    "norwegian_krone",
    "mexican_peso",
    "rand",
    "new_taiwan_dollar",
    "danish_krone",
    "zloty",
    "baht",
    "forint",
    "koruna",
    "shekel",
    "chilean_peso",
    "philippine_peso",
    "dirham",
    "colombian_peso",
    "riyal",
    "ringgit",
    "leu",
]


class Number(BaseProps):
    """
    Number database property objects

    Attributes
    ----------
    key : str
        The name of the property as it appears in Notion.
    format : FORMAT
        How the number is displayed in Notion.
    """

    def __init__(self, key: str, format: FORMAT):
        """
        Number database property objects

        Parameters
        ----------
        key : str
            The name of the property as it appears in Notion.
        format_ : FORMAT
            How the number is displayed in Notion.

        Usage
        -----
        >>> from notion_extensions.base.props.database import Number
        >>> number = Number(key="price", format="dollar")
        >>> number
        {
            'price': {
                'number': {'format': 'dollar'}
            }
        }
        """
        super().__init__()
        if format not in AVAILABLE_FORMAT:
            raise ValueError
        self.__key = key
        self[key] = {
            "number": {
                "format": "",
            }
        }

    @property
    def key(self) -> str:
        return self.__key

    @property
    def format(self) -> str:
        return self[self.__key]["number"]["format"]

    @format.setter
    def format(self, value: str) -> None:
        if value not in AVAILABLE_FORMAT:
            raise ValueError
        self[self.__key]["number"]["format"] = value
