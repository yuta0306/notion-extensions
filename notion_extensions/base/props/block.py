import sys
from typing import Dict, List, Optional, Union

from .common import BaseProps, Emoji, FileObject, Icon, Text, RichText

if sys.version_info >= (3, 8):  # "from typing" in Python 3.9 and earlier
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info > (3, 9):  # "from typing_extensions" in Python 3.9 and earlier
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

__all__ = [
    "Block",
    "Children",
    "Paragraph",
    "Heading1",
    "Heading2",
    "Heading3",
    "Callout",
    "Quote",
    "BulletedListItem",
    "BulletedList",
    "NumberedListItem",
    "NumberedList",
    "ToDo",
    "ToDoList",
    "Toggle",
    "Code",
    "Embed",
    "Image",
    "Video",
]

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

LANGUAGES: TypeAlias = Literal[
    "abap",
    "arduino",
    "bash",
    "basic",
    "c",
    "clojure",
    "coffeescript",
    "c++",
    "c#",
    "css",
    "dart",
    "diff",
    "docker",
    "elixir",
    "elm",
    "erlang",
    "flow",
    "fortran",
    "f#",
    "gherkin",
    "glsl",
    "go",
    "graphql",
    "groovy",
    "haskell",
    "html",
    "java",
    "javascript",
    "json",
    "julia",
    "kotlin",
    "latex",
    "less",
    "lisp",
    "livescript",
    "lua",
    "makefile",
    "markdown",
    "markup",
    "matlab",
    "mermaid",
    "nix",
    "objective-c",
    "ocaml",
    "pascal",
    "perl",
    "php",
    "plain text",
    "powershell",
    "prolog",
    "protobuf",
    "python",
    "r",
    "reason",
    "ruby",
    "rust",
    "sass",
    "scala",
    "scheme",
    "scss",
    "shell",
    "sql",
    "swift",
    "typescript",
    "vb.net",
    "verilog",
    "vhdl",
    "visual basic",
    "webassembly",
    "xml",
    "yaml",
    "java/c/c++/c#",
]

EMBED_PLATFORMS = [
    "Framer",
    "Twitter (tweets)",
    "Google Drive documents",
    "Gist",
    "Figma",
    "Invision,",
    "Loom",
    "Typeform",
    "Codepen",
    "PDFs",
    "Google Maps",
    "Whimisical",
    "Miro",
    "Abstract",
    "excalidraw",
    "Sketch",
    "Replit",
]

IMAGE_EXT: List[str] = [
    "png",
    "jpg",
    "jpeg",
    "gif",
    "tif",
    "tiff",
    "bmp",
    "svg",
    "heic",
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
    text : RichText
        text
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
        """
        Parameters
        ----------
        *text : Text or RichText
            text
        children : Children, optional
            children
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


class BulletedListItem(Block):
    """
    BulletedListItem
    BulletedListItem property values of block

    Attributes
    ----------
    *text : Text or RichText
        text
    children : Children, optional
        children

    Methods
    -------
    clear()
        Clear data of title
    json()
        Return this class as dictionary
    """

    TEMPLATE: Dict[str, Union[str, Dict]] = {
        "type": "bulleted_list_item",
        "bulleted_list_item": {
            "text": [],
        },
    }

    def __init__(
        self,
        *text: Union[Text, RichText],
        children: Optional[Children] = None,
    ):
        """
        Parameters
        ----------
        *text : Text or RichText
            text
        children : Children, optional
            children
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
        self["bulleted_list_item"].update(self.__text)  # Add Texts with RichText Style
        if children is not None:
            self["bulleted_list_item"].update(
                children
            )  # if children exists, Add Chilren

    @property
    def text(self) -> RichText:
        return self.__text

    @text.setter
    def text(self, value: RichText) -> None:
        if value.key != "text":
            raise ValueError("RichText's key is must be `text`")
        self.__text = value
        self["bulleted_list_item"].update(self.__text)

    @property
    def children(self) -> Children:
        return self["bulleted_list_item"]["children"]

    @children.setter
    def children(self, value: Children) -> None:
        self["bulleted_list_item"].update(value)


class BulletedList(Children):
    """
    BulletedList
    BulletedList property values of block

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
        *item: BulletedListItem,
    ):
        """
        Parameters
        ----------
        *item : BulletedListItem
            items of bulleted list item
        """
        super().__init__(*item)


class NumberedListItem(Block):
    """
    NumberedListItem
    NumberedListItem property values of block

    Attributes
    ----------
    *text : Text or RichText
        text
    children : Children, optional
        children

    Methods
    -------
    clear()
        Clear data of title
    json()
        Return this class as dictionary
    """

    TEMPLATE: Dict[str, Union[str, Dict]] = {
        "type": "numbered_list_item",
        "numbered_list_item": {
            "text": [],
        },
    }

    def __init__(
        self,
        *text: Union[Text, RichText],
        children: Optional[Children] = None,
    ):
        """
        Parameters
        ----------
        *text : Text or RichText
            text
        children : Children, optional
            children
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
        self["numbered_list_item"].update(self.__text)  # Add Texts with RichText Style
        if children is not None:
            self["numbered_list_item"].update(
                children
            )  # if children exists, Add Chilren

    @property
    def text(self) -> RichText:
        return self.__text

    @text.setter
    def text(self, value: RichText) -> None:
        if value.key != "text":
            raise ValueError("RichText's key is must be `text`")
        self.__text = value
        self["numbered_list_item"].update(self.__text)

    @property
    def children(self) -> Children:
        return self["numbered_list_item"]["children"]

    @children.setter
    def children(self, value: Children) -> None:
        self["numbered_list_item"].update(value)


class NumberedList(Children):
    """
    NumberedList
    NumberedList property values of block

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
        *item: NumberedListItem,
    ):
        """
        Parameters
        ----------
        *item : NumberedListItem
            items of numbered list item
        """
        super().__init__(*item)


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


class Toggle(Block):
    """
    Toggle
    Toggle property values of block

    Attributes
    ----------
    text : RichText
        Rich text in the toggle block
    children : Children
        Any nested children blocks of the toggle block

    Methods
    -------
    clear()
        Clear data of title
    json()
        Return this class as dictionary
    """

    TEMPLATE: Dict[str, Union[str, Dict, bool]] = {
        "type": "toggle",
        "toggle": {
            "text": [],
            "children": [],
        },
    }

    def __init__(
        self,
        *text: Union[Text, RichText],
        children: Optional[Children] = None,
    ):
        """
        Parameters
        ----------
        *text : RichText
            Rich text in the toggle block
        children : Children
            Any nested children blocks of the toggle block
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
        self["toggle"].update(self.__text)  # Add Texts with RichText Style
        if children is not None:
            self["toggle"].update(children)  # if children exists, Add Chilren

    @property
    def text(self) -> RichText:
        return self.__text

    @text.setter
    def text(self, value: RichText) -> None:
        if value.key != "text":
            raise ValueError("RichText's key is must be `text`")
        self.__text = value
        self["toggle"].update(self.__text)

    @property
    def children(self) -> Children:
        return self["toggle"]["children"]

    @children.setter
    def children(self, value: Children) -> None:
        self["toggle"].update(value)


class Code(Block):
    """
     Code
     Code property values of block

    Attributes
    ----------
    text : RichText
        Rich text in code block
    language : str, optional
        Coding language in code block
    valid_language : Literal
        Possible values for language

    Methods
    -------
    clear()
        Clear data of title
    json()
        Return this class as dictionary
    """

    TEMPLATE: Dict[str, Union[str, Dict]] = {
        "type": "code",
        "code": {
            "text": [],
            "language": "",
        },
    }

    def __init__(
        self,
        *text: Union[Text, RichText],
        language: Optional[LANGUAGES] = None,
    ):
        """
        Parameters
        ----------
        *text : Text or RichText
            Rich text in code block
        language : str, optional
            Coding language in code block
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
        self["code"].update(self.__text)  # Add Texts with RichText Style
        if language is not None:
            self["code"]["language"] = language  # Add Language

    @property
    def valid_language(self):
        return LANGUAGES

    @property
    def text(self) -> RichText:
        return self.__text

    @text.setter
    def text(self, value: RichText) -> None:
        if value.key != "text":
            raise ValueError("RichText's key is must be `text`")
        self.__text = value
        self["code"].update(self.__text)

    @property
    def language(self) -> bool:
        return self["code"]["language"]

    @language.setter
    def language(self, value: LANGUAGES) -> None:
        self["code"]["language"] = value

    @language.deleter
    def language(self) -> None:
        self["code"]["language"] = ""


class Embed(Block):
    """
     Embed
     Embed property values of block

    Attributes
    ----------
    url : str
        Link to website the embed block will display

    Methods
    -------
    clear()
        Clear data of title
    json()
        Return this class as dictionary
    """

    TEMPLATE: Dict[str, Union[str, Dict]] = {
        "type": "embed",
        "embed": {
            "url": "",
        },
    }

    def __init__(
        self,
        url: str,
    ):
        """
        Parameters
        ----------
        url : str
            Link to website the embed block will display
        """
        super().__init__()
        self["embed"]["url"] = url

    @property
    def url(self) -> str:
        return self["embed"]["url"]

    @url.setter
    def url(self, value: str) -> None:
        self["embed"]["url"] = value

    @url.deleter
    def url(self) -> None:
        self["embed"]["url"] = ""


class Image(Block):
    """
     Image
     Image property values of block
     Includes supported image urls (i.e. ending in .png, .jpg, .jpeg, .gif, .tif, .tiff, .bmp, .svg, or .heic)

    Attributes
    ----------
    url : str
        Link to website the image block will display
    type_ : 'external' or 'file', default='external'
        Type of this file object. Possible values are: 'external', 'file'

    Methods
    -------
    clear()
        Clear data of title
    json()
        Return this class as dictionary
    """

    TEMPLATE: Dict[str, Union[str, Dict]] = {
        "type": "image",
        "image": {
            "type": "external",
            "external": {
                "url": "",
            },
        },
    }

    def __init__(
        self,
        url: Optional[str] = None,
        type_: Literal["external", "file"] = "external",
        file: Optional[FileObject] = None,
    ):
        """
        Parameters
        ----------
        url : str, optional
            Link to website the image block will display
        type_ : 'external' or 'file', default='external'
            Type of this file object. Possible values are: 'external', 'file'
        file : FileObject, optional
            FileObject
        """
        super().__init__()
        if url is None and file is None:
            raise ValueError("Either url or file should be not None")
        elif file is not None:
            self.__file = file
        elif url is not None:
            ext = url.split(".")[-1]
            if ext not in IMAGE_EXT:
                raise ValueError(
                    """Includes supported image urls,
                    (i.e. ending in .png, .jpg, .jpeg, .gif, .tif, .tiff, .bmp, .svg, or .heic)"""
                )
            self.__file = FileObject(type_=type_, url=url)
        self["image"] = self.__file

    @property
    def type_(self) -> str:
        return self.__file.type_

    @type_.setter
    def type_(self, value: Literal["external", "file"]) -> None:
        self.__file.type_ = value
        self["image"] = self.__file

    @type_.deleter
    def type_(self) -> None:
        self.__file.type_ = "external"
        self["image"] = self.__file

    @property
    def url(self) -> str:
        return self.__file.url

    @url.setter
    def url(self, value: str) -> None:
        self.__file.url = value

    @url.deleter
    def url(self) -> None:
        self.__file.url = ""


class Video(Block):
    """
     Video
     Video property values of block

    Attributes
    ----------
    url : str
        Link to website the video block will display
    type_ : 'external' or 'file', default='external'
        Type of this file object. Possible values are: 'external', 'file'

    Methods
    -------
    clear()
        Clear data of title
    json()
        Return this class as dictionary
    """

    TEMPLATE: Dict[str, Union[str, Dict]] = {
        "type": "video",
        "video": {
            "type": "external",
            "external": {
                "url": "",
            },
        },
    }

    def __init__(
        self,
        url: Optional[str] = None,
        type_: Literal["external", "file"] = "external",
        file: Optional[FileObject] = None,
    ):
        """
        Parameters
        ----------
        url : str, optional
            Link to website the video block will display
        type_ : 'external' or 'file', default='external'
            Type of this file object. Possible values are: 'external', 'file'
        file : FileObject, optional
            FileObject
        """
        super().__init__()
        if url is None and file is None:
            raise ValueError("Either url or file should be not None")
        elif file is not None:
            self.__file = file
        elif url is not None:
            self.__file = FileObject(type_=type_, url=url)
        self["video"] = self.__file

    @property
    def type_(self) -> str:
        return self.__file.type_

    @type_.setter
    def type_(self, value: Literal["external", "file"]) -> None:
        self.__file.type_ = value
        self["video"] = self.__file

    @type_.deleter
    def type_(self) -> None:
        self.__file.type_ = "external"
        self["video"] = self.__file

    @property
    def url(self) -> str:
        return self.__file.url

    @url.setter
    def url(self, value: str) -> None:
        self.__file.url = value

    @url.deleter
    def url(self) -> None:
        self.__file.url = ""
