import sys


if sys.version_info > (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info > (3, 9):
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
    def __init__(self, key: str, format_: FORMAT):
        super().__init__()
        if format_ not in AVAILABLE_FORMAT:
            raise ValueError
        self.key = key
        self[key] = {
            "number": {
                "format": "",
            }
        }
        self.format = format_

    @property
    def format(self) -> str:
        return self[self.key]["number"]["format"]

    @format.setter
    def format(self, value: str) -> None:
        if value not in AVAILABLE_FORMAT:
            raise ValueError
        self[self.key]["number"]["format"] = value
