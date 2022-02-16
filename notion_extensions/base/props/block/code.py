import sys
from typing import Dict, Optional, Union

if sys.version_info >= (3, 8):  # "from typing" in Python 3.9 and earlier
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 10):  # "from typing_extensions" in Python 3.9 and earlier
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

from ..common import RichText, Text
from .block import Block

__all__ = [
    "Code",
    "LANGUAGES",
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
