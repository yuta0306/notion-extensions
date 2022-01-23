from typing import Dict, Optional, Union

from .block import Block
from .children import Children
from ..common import Text, RichText

__all__ = [
    "ToDo",
    "ToDoList",
]


class ToDo(Block):
    """
    ToDo
    ToDo property values of block

    Attributes
    ----------
    text : RichText
        Text in the to_do block
    checked : bool, default=False
        Whether the to_do is checked or not
    children : Children
        Any nested children blocks of the to_do block

    Methods
    -------
    clear()
        Clear data of title
    json()
        Return this class as dictionary
    """

    TEMPLATE: Dict[str, Union[str, Dict, bool]] = {
        "type": "to_do",
        "to_do": {
            "text": [],
            "checked": False,
        },
    }

    def __init__(
        self,
        *text: Union[Text, RichText],
        checked: bool = False,
        children: Optional[Children] = None,
    ):
        """
        Parameters
        ----------
        *text : Text or RichText
            Text in the to_do block
        checked : bool, default=False
            Whether the to_do is checked or not
        children : Children, optional
            Any nested children blocks of the to_do block
        """
        super().__init__()
        base = []  # Aggregate Texts
        for t in text:
            if isinstance(t, RichText):
                base.extend(list(t[t.key]))
            elif isinstance(t, Text):
                base.append(t)
            else:
                raise ValueError(
                    f"Expected type is `RichText` or `Text`, but {type(t)} is given"
                )
        self.__text = RichText(key="text", *base)
        self["to_do"].update(self.__text)  # Add Texts with RichText Style
        self["to_do"]["checked"] = checked  # Add Checked
        if children is not None:
            self["to_do"].update(children)  # if children exists, Add Chilren

    @property
    def text(self) -> RichText:
        return self.__text

    @text.setter
    def text(self, value: RichText) -> None:
        if value.key != "text":
            raise ValueError("RichText's key is must be `text`")
        self.__text = value
        self["to_do"].update(self.__text)

    @property
    def children(self) -> Children:
        return self["to_do"]["children"]

    @children.setter
    def children(self, value: Children) -> None:
        self["to_do"].update(value)

    @property
    def checked(self) -> bool:
        return self["to_do"]["checked"]

    @checked.setter
    def checked(self, value: bool) -> None:
        self["to_do"]["checked"] = value

    @checked.deleter
    def checked(self) -> None:
        self["to_do"]["checked"] = False


class ToDoList(Children):
    """
    ToDoList
    ToDoList property values of block

    Attributes
    ----------

    Methods
    -------
    clear()
        Clear data of title
    json()
        Return this class as dictionary
    """

    def __init__(
        self,
        *item: ToDo,
    ):
        """
        Parameters
        ----------
        *item : ToDo
            items of todo item
        """
        super().__init__(*item)
