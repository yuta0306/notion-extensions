import json
from typing import Any, Dict, Final, List, NoReturn, Tuple, Union, Optional
try:
    from typing import Literal
except:
    from typing_extensions import Literal
import os

import requests

from .props.page import Title

PAGE_PROPERTY = Dict[str, Any]
BLOCK_OBJECT = Dict[str, Any]
PAGE_ICON = Dict[str, Any]
PAGE_COVER = Dict[str, Any]

# Type Hint
UrlLike = str

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
    def __init__(self, *, key: Optional[str] = None, name: str = 'NOTION_KEY'):
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
                raise ValueError(f'if `key` is None, global environment must have `{name}`.')
        
        self.__key: Final[str] = key
        self.__version: Final[str] = '2021-08-16'
        self.__headers: Final[Dict[str, str]] = {
            'Notion-Version': self.version,
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.key}',
        }

    # Properties
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

    @property
    def headers(self) -> Dict[str, str]:
        """
        Headers using for access API endpoints
        """
        return self.__headers

    # Special Methods
    def __str__(self) -> str:
        mask = '*' * len(self.key)
        return f'NotionClient\n::   key   :: {mask}\n:: version :: {self.version}\n'

    def __repr__(self) -> str:
        mask = '*' * len(self.key)
        return f'NotionClient\n::   key   :: {mask}\n:: version :: {self.version}\n'

    # Private Methods
    def _parse_id(self, urllike: UrlLike) -> str:
        """
        Parameters
        ----------
        urllike : UrlLike

        Returns
        -------
        str
            ID from URL format
        """
        id_ = urllike.split('/')[-1]  # retrieve the last string
        id_ = id_.split('-')[-1]  # remove string like title
        id_ = id_.split('?')[0]  # remove params of url
        return id_

    # Pages
    def get_page(self, *, page_id: Union[str, UrlLike]) -> Tuple[int, Dict[str, Any]]:  # get a page
        """
        Get a page with page_id

        Parameters
        ----------
        page_id : str or UrlLike
            ID of the page you can get

        Returns
        -------
        Tuple[int, Dict[str, Any]]
            This returns status_code and response of dictionary
        """
        page_id = self._parse_id(page_id)
        res = requests.get(f'https://api.notion.com/v1/pages/{page_id}',
                           headers=self.headers)
        return res.status_code, res.json()

    def create_page(self, *, parent_id: Optional[Union[str, UrlLike]], parent_type: Literal['database', 'page'],
                    properties: Title, children: Optional[List[BLOCK_OBJECT]] = None, icon: Optional[PAGE_ICON] = None,
                    cover: Optional[PAGE_COVER] = None) -> Tuple[int, Dict[str, Any]]:  # create a page
        """
        Create a page with page_id

        Parameters
        ----------
        parent_type : 'database' or 'page'
            parent type of the page you will create
        properties : Title or Dict
            properties of the page you will create
            using Title class is recommended
        parent_id : str or UrlLike, optional
            ID of the parent database or page, or URL of the parent database or page
        children : List of BlockObject, optional
            List of a block object
        icon : Icon, optional
            Icon of a page
        cover : Cover, optional
            Cover of a page

        Returns
        -------
        Tuple[int, Dict[str, Any]]
            This returns status_code and response of dictionary
        """
        if parent_type not in ('database', 'page'):  # parent_type must be `database` or `page`
            raise ValueError('`parent_type` must be database or page')
        parent_type = f'{parent_type}_id'
        parent_id = self._parse_id(parent_id)
                
        # set params
        body = {
            'parent': {
                parent_type: parent_id,
            },
            'properties': {
                'title': properties.json(),
            },
            'children': children if children is not None else [],
            'icon': icon,
            'cover': cover,
        }
        # create a page
        res = requests.post(f'https://api.notion.com/v1/pages/',
                           headers=self.headers, data=json.dumps(body))

        return res.status_code, res.json()

    # Blocks
    def get_block(self, *, block_id: str) -> Tuple[int, Dict[str, Any]]:
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
        res = requests.get(f'https://api.notion.com/v1/blocks/{block_id}',
                           headers=self.headers)
        return res.status_code, res.json()

    def get_child_blocks(self, *, block_id: str, start_cursor: Optional[str] = None) -> Tuple[int, Dict[str, Any]]:
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
        params = {
            'page_size': 100,  # max size of page_size
            'start_cursor': start_cursor,
        }
        res = requests.get(f'https://api.notion.com/v1/blocks/{block_id}/children',
                           headers=self.headers, params=params)
        return res.status_code, res.json()