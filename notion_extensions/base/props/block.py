import sys
from typing import Dict, List, Optional, Union

from .common import BaseProps, Emoji, Icon, Text, RichText

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

BLOCK_TYPES = Literal[
    "paragraph",
    "heading_1",
    "heading_2",
    "heading_3",
    "bulleted_list_item",
    "numbered_list_item",
    "to_do",
    "toggle",
    "child_page",
    "child_database",
    "embed",
    "image",
    "video",
    "file",
    "pdf",
    "bookmark",
    "callout",
    "quote",
    "equation",
    "divider",
    "table_of_contents",
    "column",
    "column_list",
    "link_preview",
    "synced_block",
    "template",
    "link_to_page",
    "table",
    "table_row",
    "unsupported",
    "children",
]


class Block(BaseProps):
    def __init__(self):
        super().__init__()


class Children(Block):
    """
    Children
    Children property values of block

    Attributes
    ----------

    Methods
    -------
    clear()
        Clear data of title
    json()
        Return this class as dictionary
    """

    TEMPLATE: Dict[str, List[Block]] = {"children": []}

    def __init__(
        self,
        *block: Block,
    ):
        super().__init__()
        self.__blocks = list(block)
        self["children"] = self.__blocks

    def __add__(self, other: Union[Block, List[Block]]):
        if isinstance(other, list):
            self.extend(other)
            return self
        self.append(other)
        return self

    def __iadd__(self, other: Union[Block, List[Block]]):
        return self.__add__(other)

    def append(self, block: Block) -> None:
        """
        append(block: Block)
            Append Block to existing list of Block

        Parameters
        ----------
        block : Block
            Block you append to Children
        """
        self.__blocks.append(block)
        self["children"] = self.__blocks

    def extend(self, blocks: List[Block]) -> None:
        """
        extens(blocks: List[Block])
            Append Block to existing list of Block

        Parameters
        ----------
        blocks : list of Block
            List of block you append to Children
        """
        self.__blocks.extend(blocks)
        self["children"] = self.__blocks

    def insert(self, index: int, block: Block) -> None:
        """
        insert(index: int, block: Block)
            Append block to existing list of Block

        Parameters
        ----------
        index : int
            Index you insert Block into Children
        block : Block
            Block you insert into Children
        """
        self.__blocks.insert(index, block)
        self["children"] = self.__blocks

    def pop(self, index=None):
        """
        pop(Block: Block)
            Pop Block to existing list of Block

        Parameters
        ----------
        index : int, default=None
            Block you pop from RichBlock
        """
        item = self.__blocks.pop(index)
        self["children"] = self.__blocks
        return item


class Paragraph(Block):
    """
    Paragraph
    Paragraph property values of block

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
        "object": "block",
        "type": "paragraph",
        "paragraph": {
            "text": [],
        },
    }

    def __init__(
        self,
        *text: Union[Text, RichText],
    ):
        super().__init__()
        base = []
        for t in text:
            if isinstance(t, RichText):
                base.extend(list(t[t.key]))
            elif isinstance(t, Text):
                base.append(t)
            else:
                raise ValueError(
                    f"Expected type is `RichText` or `Text`, but {type(t)} is given"
                )
        self.__texts = RichText(key="text", *base)

        self.update(
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": self.__texts,
            },
        )

    def __add__(self, other: Union[Text, List[Text]]):
        if isinstance(other, list):
            self.extend(other)
            return self
        self.append(other)
        return self

    def __iadd__(self, other: Union[Text, List[Text]]):
        return self.__add__(other)

    def append(self, text: Text) -> None:
        """
        append(text: Text)
            Append Text to existing list of Text

        Parameters
        ----------
        text : Text
            Text you append to RichText
        """
        self.__texts.append(text)
        self["paragraph"] = self.__texts

    def extend(self, texts: List[Text]) -> None:
        """
        extens(texts: Text)
            Append Text to existing list of Text

        Parameters
        ----------
        text : list of Text
            List of text you append to RichText
        """
        self.__texts.extend(texts)
        self["paragraph"] = self.__texts

    def insert(self, index: int, text: Text) -> None:
        """
        insert(index: int, text: Text)
            Append Text to existing list of Text

        Parameters
        ----------
        index : int
            Index you insert Text into
        text : Text
            Text you insert into RichText
        """
        self.__texts.insert(index, text)
        self["paragraph"] = self.__texts

    def pop(self, index=None):
        """
        pop(text: Text)
            Pop Text to existing list of Text

        Parameters
        ----------
        index : int, default=None
            Text you pop from RichText
        """
        item = self.__texts.pop(index)
        self["paragraph"] = self.__texts
        return item


class Heading1(Block):
    """
    Heading1
    Heading1 property values of block

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
        "object": "block",
        "type": "heading_1",
        "heading_1": {
            "text": [],
        },
    }

    def __init__(
        self,
        *text: Union[RichText, Text],
    ):
        super().__init__()
        base = []
        for t in text:
            if isinstance(t, RichText):
                base.extend(list(t[t.key]))
            elif isinstance(t, Text):
                base.append(t)
            else:
                raise ValueError(
                    f"Expected type is `RichText` or `Text`, but {type(t)} is given"
                )
        self.__texts = RichText(key="text", *base)

        self.update(
            {
                "object": "block",
                "type": "heading_1",
                "heading_1": self.__texts,
            },
        )

    def __add__(self, other: Union[Text, List[Text]]):
        if isinstance(other, list):
            self.extend(other)
            return self
        self.append(other)
        return self

    def __iadd__(self, other: Union[Text, List[Text]]):
        return self.__add__(other)

    def append(self, text: Text) -> None:
        """
        append(text: Text)
            Append Text to existing list of Text

        Parameters
        ----------
        text : Text
            Text you append to RichText
        """
        self.__texts.append(text)
        self["heading_1"] = self.__texts

    def extend(self, texts: List[Text]) -> None:
        """
        extens(texts: Text)
            Append Text to existing list of Text

        Parameters
        ----------
        text : list of Text
            List of text you append to RichText
        """
        self.__texts.extend(texts)
        self["heading_1"] = self.__texts

    def insert(self, index: int, text: Text) -> None:
        """
        insert(index: int, text: Text)
            Append Text to existing list of Text

        Parameters
        ----------
        index : int
            Index you insert Text into
        text : Text
            Text you insert into RichText
        """
        self.__texts.insert(index, text)
        self["heading_1"] = self.__texts

    def pop(self, index=None):
        """
        pop(text: Text)
            Pop Text to existing list of Text

        Parameters
        ----------
        index : int, default=None
            Text you pop from RichText
        """
        item = self.__texts.pop(index)
        self["heading_1"] = self.__texts
        return item


class Heading2(Block):
    """
    Heading2
    Heading2 property values of block

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
        "object": "block",
        "type": "heading_2",
        "heading_2": {
            "text": [],
        },
    }

    def __init__(
        self,
        *text: Union[RichText, Text],
    ):
        super().__init__()
        base = []
        for t in text:
            if isinstance(t, RichText):
                base.extend(list(t[t.key]))
            elif isinstance(t, Text):
                base.append(t)
            else:
                raise ValueError(
                    f"Expected type is `RichText` or `Text`, but {type(t)} is given"
                )
        self.__texts = RichText(key="text", *base)

        self.update(
            {
                "object": "block",
                "type": "heading_2",
                "heading_2": self.__texts,
            },
        )

    def __add__(self, other: Union[Text, List[Text]]):
        if isinstance(other, list):
            self.extend(other)
            return self
        self.append(other)
        return self

    def __iadd__(self, other: Union[Text, List[Text]]):
        return self.__add__(other)

    def append(self, text: Text) -> None:
        """
        append(text: Text)
            Append Text to existing list of Text

        Parameters
        ----------
        text : Text
            Text you append to RichText
        """
        self.__texts.append(text)
        self["heading_2"] = self.__texts

    def extend(self, texts: List[Text]) -> None:
        """
        extens(texts: Text)
            Append Text to existing list of Text

        Parameters
        ----------
        text : list of Text
            List of text you append to RichText
        """
        self.__texts.extend(texts)
        self["heading_2"] = self.__texts

    def insert(self, index: int, text: Text) -> None:
        """
        insert(index: int, text: Text)
            Append Text to existing list of Text

        Parameters
        ----------
        index : int
            Index you insert Text into
        text : Text
            Text you insert into RichText
        """
        self.__texts.insert(index, text)
        self["heading_2"] = self.__texts

    def pop(self, index=None):
        """
        pop(text: Text)
            Pop Text to existing list of Text

        Parameters
        ----------
        index : int, default=None
            Text you pop from RichText
        """
        item = self.__texts.pop(index)
        self["heading_2"] = self.__texts
        return item


class Heading3(Block):
    """
    Heading3
    Heading3 property values of block

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
        "object": "block",
        "type": "heading_3",
        "heading_3": {
            "text": [],
        },
    }

    def __init__(
        self,
        *text: Union[RichText, Text],
    ):
        super().__init__()
        base = []
        for t in text:
            if isinstance(t, RichText):
                base.extend(list(t[t.key]))
            elif isinstance(t, Text):
                base.append(t)
            else:
                raise ValueError(
                    f"Expected type is `RichText` or `Text`, but {type(t)} is given"
                )
        self.__texts = RichText(key="text", *base)

        self.update(
            {
                "object": "block",
                "type": "heading_3",
                "heading_3": self.__texts,
            },
        )

    def __add__(self, other: Union[Text, List[Text]]):
        if isinstance(other, list):
            self.extend(other)
            return self
        self.append(other)
        return self

    def __iadd__(self, other: Union[Text, List[Text]]):
        return self.__add__(other)

    def append(self, text: Text) -> None:
        """
        append(text: Text)
            Append Text to existing list of Text

        Parameters
        ----------
        text : Text
            Text you append to RichText
        """
        self.__texts.append(text)
        self["heading_3"] = self.__texts

    def extend(self, texts: List[Text]) -> None:
        """
        extens(texts: Text)
            Append Text to existing list of Text

        Parameters
        ----------
        text : list of Text
            List of text you append to RichText
        """
        self.__texts.extend(texts)
        self["heading_3"] = self.__texts

    def insert(self, index: int, text: Text) -> None:
        """
        insert(index: int, text: Text)
            Append Text to existing list of Text

        Parameters
        ----------
        index : int
            Index you insert Text into
        text : Text
            Text you insert into RichText
        """
        self.__texts.insert(index, text)
        self["heading_3"] = self.__texts

    def pop(self, index=None):
        """
        pop(text: Text)
            Pop Text to existing list of Text

        Parameters
        ----------
        index : int, default=None
            Text you pop from RichText
        """
        item = self.__texts.pop(index)
        self["heading_3"] = self.__texts
        return item


class Callout(Block):
    """
    Callout
    Callout property values of block

    Attributes
    ----------
    text : RichText
        text
    icon : Icon
        icon
    children : Children
        children

    Methods
    -------
    clear()
        Clear data of title
    json()
        Return this class as dictionary
    """

    TEMPLATE: Dict[str, Union[str, Dict]] = {
        "type": "callout",
        "callout": {
            "text": [],
        },
    }

    def __init__(
        self,
        *text: Union[Text, RichText],
        icon: Icon = Icon(Emoji("")),
        children: Optional[Children] = None,
    ):
        """
        Parameters
        ----------
        *text : Text or RichText
            text
        icon : Icon, defalut=Icon(Emoji(""))
            icon
        children : Children, optional
            children
        """
        super().__init__()
        self["callout"].update(icon)  # Add Icon
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
        self["callout"].update(self.__text)  # Add Texts with RichText Style
        if children is not None:
            self["callout"].update(children)  # if children exists, Add Chilren

    @property
    def text(self) -> RichText:
        return self.__text

    @text.setter
    def text(self, value: RichText) -> None:
        if value.key != "text":
            raise ValueError("RichText's key is must be `text`")
        self.__text = value
        self["callout"].update(self.__text)

    @property
    def icon(self) -> Icon:
        return self["callout"]["icon"]

    @icon.setter
    def icon(self, value: Icon) -> None:
        self["callout"].update(value)

    @property
    def children(self) -> Children:
        return self["callout"]["children"]

    @children.setter
    def children(self, value: Children) -> None:
        self["callout"].update(value)


class Quote(Block):
    """
    Quote
    Quote property values of block

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
        "type": "quote",
        "quote": {
            "text": [],
        },
    }

    def __init__(
        self,
        *text: Union[Text, RichText],
        children: Optional[Children] = None,
    ):
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
        self["quote"].update(self.__text)  # Add Texts with RichText Style
        if children is not None:
            self["quote"].update(children)  # if children exists, Add Chilren

    @property
    def text(self) -> RichText:
        return self.__text

    @text.setter
    def text(self, value: RichText) -> None:
        if value.key != "text":
            raise ValueError("RichText's key is must be `text`")
        self.__text = value
        self["quote"].update(self.__text)

    @property
    def children(self) -> Children:
        return self["quote"]["children"]

    @children.setter
    def children(self, value: Children) -> None:
        self["quote"].update(value)
