from typing import Any, Dict, Final, NoReturn, Tuple, Union, Optional
import os

import requests

class NotionClient:
    """
    NotionClient

    Attributes
    ----------
    key : str
        API key of Notion
    version : str
        Notion version used for authorization

    Methods
    -------
    get_page(page_id: str)
        Get a page with page_id.
    get_blocks(block_id: str)
        Get a block with block_id.
    get_child_blocks(block_id: str, start_cursor: Optional[str])
        Get child blocks with block_id
    """
    def __init__(self, key: Optional[str] = None, name: str = 'NOTION_KEY') -> NoReturn:
        """
        Parameters
        ----------
        key : str, optional
            API key of Notion
        name : str, default='NOTION_KEY'
            Name of the environment variable which has API key of Notion.
            If key is not given, name is used for getting API key.
            `name='NOTION_KEY'` as default.
        """
        if key is None:
            key = os.environ.get(name)
            if key is None:
                raise ValueError(f'if `key` is None, global environment must have {name}.')
        
        self.__key = key
        self.__version: Final[str] = '2021-08-16'

    @property
    def key(self) -> str:
        """
        API key of Notion
        """
        return self.__key

    @property
    def version(self) -> str:
        """
        Notion version used for authorization
        """
        return self.__version

    def get_page(self, page_id: str) -> Tuple[int, Dict[str, Any]]:
        """
        Get a page with page_id

        Parameters
        ----------
        page_id : str
            ID of the page you can get

        Returns
        -------
        Tuple[int, Dict[str, Any]]
            This returns status_code and response of dictionary
        """
        headers = {
            'Notion-Version': self.version,
            'Authorization': f'Bearer {self.key}',
        }
        res = requests.get(f'https://api.notion.com/v1/pages/{page_id}',
                            headers=headers)
        return res.status_code, res.json()

    def get_block(self, block_id: str) -> Tuple[int, Dict[str, Any]]:
        """
        Get a block with block_id

        Parameters
        ----------
        block_id : str
            ID of the block you can get

        Returns
        -------
        Tuple[int, Dict[str, Any]]
            This returns status_code and response of dictionary
        """
        headers = {
            'Notion-Version': self.version,
            'Authorization': f'Bearer {self.key}',
        }
        res = requests.get(f'https://api.notion.com/v1/blocks/{block_id}',
                            headers=headers)
        return res.status_code, res.json()

    def get_child_blocks(self, block_id: str, start_cursor: Optional[str] = None) -> Tuple[int, Dict[str, Any]]:
        """
        Get child blocks with block_id

        Parameters
        ----------
        block_id : str
            ID of the block you can get
        start_cursor : str, optional
            Cursor of pagination for getting child blocks

        Returns
        -------
        Tuple[int, Dict[str, Any]]
            This returns status_code and response of dictionary
        """
        headers = {
            'Notion-Version': self.version,
            'Authorization': f'Bearer {self.key}',
        }
        params = {
            'page_size': 100,  # max size of page_size
            'start_cursor': start_cursor,
        }
        res = requests.get(f'https://api.notion.com/v1/blocks/{block_id}/children',
                            headers=headers, params=params)
        return res.status_code, res.json()