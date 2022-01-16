import sys

if sys.version_info > (3, 9):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

UrlLike: TypeAlias = str


def parse_id(
    id_: UrlLike,
    type_: Literal["page", "database", "block"],
) -> str:
    id_ = id_.split("/")[-1]
    if type_ in ("page"):
        id_ = id_.split("-")[-1]  # remove string like title
    elif type_ in ("database"):
        id_ = id_.split("?")[0]  # remove body of url
    elif type_ in ("block"):
        id_ = id_.split("#")[-1]  # remove page link
    else:
        raise ValueError("type_ must be `page` or `database` or `block`")
    return id_
