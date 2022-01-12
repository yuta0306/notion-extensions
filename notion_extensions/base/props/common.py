from collections import UserDict
from typing import Any, Dict, Final, List, NoReturn, Tuple, Union, Optional
try:
    from typing import Literal
except:
    from typing_extensions import Literal

class BaseProps(UserDict):
    TEMPLATE: Dict = {}
    def __init__(self):
        super().__init__()
        self.data = BaseProps.TEMPLATE

    def __setitem__(self, key: str, item: Any) -> NoReturn:
        return super().__setitem__(key, item)

    def __delitem__(self, key) -> NoReturn:
        """
        Raises
        ------
        NotImplementedError
        """
        raise NotImplementedError

    def pop(self):
        """
        pop()

        Raises
        ------
        NotImplementedError
        """
        raise NotImplementedError

    def popitem(self):
        """
        popitem()

        Raises
        ------
        NotImplementedError
        """
        raise NotImplementedError

    def clear(self) -> NoReturn:
        """
        clear()

        Returns
        -------
        NoReturn
        """
        self.data = self.TEMPLATE

    def update(self) -> NoReturn:
        """
        Raises
        ------
        NotImplementedError
        """
        raise NotImplementedError

    def setdefault(self, __key, __default):
        """
        Raises
        ------
        NotImplementedError
        """
        raise NotImplementedError