from typing import Dict, Union

from .block import Block

__all__ = [
    "Equation",
]


class Equation(Block):
    """
    Equation
    Equation property values of block

    Attributes
    ----------
    expression : str
        A KaTeX compatible string

    Methods
    -------
    clear()
        Clear data of title
    json()
        Return this class as dictionary
    """

    TEMPLATE: Dict[str, Union[str, Dict]] = {
        "type": "equation",
        "equation": {"expression": ""},
    }

    def __init__(
        self,
        expression: str,
    ):
        """
        Parameters
        ----------
        expression : str
            A KaTeX compatible string

        Usage
        -----
        >>> from notion_extensions.base.props.block import Equation
        >>> equation = "y = x_1 ^ 2 + x_2 ^2"
        >>> equation = Equation(equation)
        >>> equation
        {'type': 'equation', 'equation': {'expression': 'y = x_1 ^ 2 + x_2 ^2'}}
        """
        super().__init__()
        self["equation"]["expression"] = expression

    @property
    def expression(self) -> str:
        return self["equation"]["expression"]

    @expression.setter
    def expression(self, value: str) -> None:
        self["equation"]["expression"] = value

    @expression.deleter
    def expression(self) -> None:
        self["equation"]["expression"] = ""
