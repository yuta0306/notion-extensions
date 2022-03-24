import json
import os
import sys
import warnings
from typing import Any, Dict, Final, Optional, Tuple, Union

import requests
from notion_extensions.base.props.block import Children
from notion_extensions.base.props.common import Cover, Icon, RichText

from .props.page import Title

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

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

    def __init__(self, *, key: Optional[str] = None, name: str = "NOTION_KEY"):
        """
        Parameters
        ----------
        key : str, optional
            API key of Notion
        name : str, default='NOTION_KEY'
            Name of the environment variable which has API key of Notion.
            If key is not given, name is used for getting API key.
            `name='NOTION_KEY'` as default.

        Usage
        ------
        >>> from notion_extensions import NotionClient
        >>> client=NotionClient()
        >>> client
        NotionClient
        ::   key   :: **************************************************
        :: version :: 2021-08-16
        """
        if key is None:
            key = os.environ.get(name)
            if key is None:
                raise ValueError(
                    f"if `key` is None, global environment must have `{name}`."
                )

        self.__key: Final[str] = key
        self.__version: Final[str] = "2022-02-22"
        self.__headers: Final[Dict[str, str]] = {
            "Notion-Version": self.version,
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.key}",
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
        mask = "*" * len(self.key)
        return f"NotionClient\n::   key   :: {mask}\n:: version :: {self.version}\n"

    def __repr__(self) -> str:
        mask = "*" * len(self.key)
        return f"NotionClient\n::   key   :: {mask}\n:: version :: {self.version}\n"

    # Private Methods
    def _parse_id(
        self, urllike: UrlLike, type_: Literal["page", "database", "block"] = "page"
    ) -> str:
        """
        Parameters
        ----------
        urllike : UrlLike

        Returns
        -------
        str
            ID from URL format
        """
        id_ = urllike.split("/")[-1]  # retrieve the last string
        if type_ in ("page"):
            id_ = id_.split("-")[-1]  # remove string like title
        elif type_ in ("database"):
            id_ = id_.split("?")[0]  # remove body of url
        elif type_ in ("block"):
            id_ = id_.split("#")[-1]  # remove page link
        else:
            raise ValueError("type_ must be `page` or `database` or `block`")
        return id_

    # Databases
    def get_database(
        self,
        *,
        database_id: Union[str, UrlLike],
    ) -> Tuple[int, Dict[str, Any]]:  # get a page
        """
        Get a database with database_id

        Parameters
        ----------
        database_id : str or UrlLike
            ID or URL of the database you can get

        Returns
        -------
        Tuple[int, Dict[str, Any]]
            This returns status_code and response of dictionary
        """
        database_id = self._parse_id(database_id, type_="database")
        res = requests.get(
            f"https://api.notion.com/v1/databases/{database_id}", headers=self.headers
        )
        return res.status_code, res.json()

    def create_database(
        self,
        *,
        parent_page_id: Union[str, UrlLike],
        properties: Dict,
        title: Optional[RichText] = None,
        icon: Optional[Icon] = None,
    ) -> Tuple[int, Dict[str, Any]]:  # get a page
        """
        Get a database with database_id

        Parameters
        ----------
        database_id : str or UrlLike
            ID or URL of the database you can get

        Returns
        -------
        Tuple[int, Dict[str, Any]]
            This returns status_code and response of dictionary
        """
        parent_page_id = self._parse_id(parent_page_id, type_="page")
        body = {
            "parent": {
                "type": "page_id",
                "page_id": parent_page_id,
            },
        }
        body.update(properties)
        if title is not None:
            title.key = "title"
            body.update(title)
        if icon is not None:
            body.update(icon)

        res = requests.post(
            "https://api.notion.com/v1/databases/",
            headers=self.headers,
            data=json.dumps(body),
        )
        return res.status_code, res.json()

    # Pages
    def get_page(
        self,
        *,
        page_id: Union[str, UrlLike],
    ) -> Tuple[int, Dict[str, Any]]:  # get a page
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

        Usage
        -----
        >>> from notion_extensions import NotionClient
        >>> client=NotionClient()
         client.get_page(page_id="https...")

        """
        page_id = self._parse_id(page_id)
        res = requests.get(
            f"https://api.notion.com/v1/pages/{page_id}", headers=self.headers
        )
        return res.status_code, res.json()

    def create_page(
        self,
        *,
        parent_id: Union[str, UrlLike],
        parent_type: Literal["database", "page"],
        properties: Title,
        children: Optional[Children] = None,
        icon: Optional[Icon] = None,
        cover: Optional[Cover] = None,
    ) -> Tuple[int, Dict[str, Any]]:  # create a page
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
            Page content for the new page as an array of block objects
        icon : Icon, optional
            Icon of a page
        cover : Cover, optional
            Cover of a page

        Returns
        -------
        Tuple[int, Dict[str, Any]]
            This returns status_code and response of dictionary

        Usage
        -----
        >>> from notion_extensions import NotionClient
        >>> client=NotionClient()
        >>> from notion_extensions.base.props.page import Title
        >>> title = Title(title="SamplePage")
        >>> client.create_page(parent_id=url, parent_type="page", properties=title)
        """
        if parent_type not in (
            "database",
            "page",
        ):  # parent_type must be `database` or `page`
            raise ValueError("`parent_type` must be database or page")
        parent_id = self._parse_id(parent_id, type_=parent_type)  # parse ID from URL
        parent_type = f"{parent_type}_id"

        # set body
        body = {
            "parent": {
                parent_type: parent_id,
            },
            "properties": properties,
        }
        if children is not None:  # Add children
            body.update(children)
        if icon is not None:  # Add icon
            body.update(icon)
        if cover is not None:  # Add cover
            body.update(cover)

        # create a page
        res = requests.post(
            "https://api.notion.com/v1/pages/",
            headers=self.headers,
            data=json.dumps(body),
        )

        return res.status_code, res.json()

    def update_page(
        self,
        *,
        page_id: Union[str, UrlLike],
        properties: Optional[Title] = None,
        archived: bool = False,
        icon: Optional[Icon] = None,
        cover: Optional[Cover] = None,
    ) -> Tuple[int, Dict[str, Any]]:  # create a page
        """
        Update a page with page_id

        Parameters
        ----------
        page_id : str or UrlLike, optional
            ID of the parent page, or URL of the parent page
        properties : Title
            properties of the page you will update
        archived : bool, default=False
            Set to True to archive (delete) a page. Set to False to un-archive (restore) a page
        icon : Icon, optional
            Icon of a page
        cover : Cover, optional
            Cover of a page

        Returns
        -------
        Tuple[int, Dict[str, Any]]
            This returns status_code and response of dictionary

        .. note:: Implement children, icon, cover
        """
        page_id = self._parse_id(page_id, type_="page")  # parse ID from URL

        # set body
        body: dict = {
            "archived": archived,
        }
        if properties is not None:
            body["properties"] = properties
        if icon is not None:  # Add icon
            body.update(icon)
        if cover is not None:  # Add cover
            body.update(cover)

        # update page
        res = requests.patch(
            f"https://api.notion.com/v1/pages/{page_id}",
            headers=self.headers,
            data=json.dumps(body),
        )

        return res.status_code, res.json()

    def delete_page(
        self,
        *,
        page_id: Union[str, UrlLike],
    ) -> Tuple[int, Dict[str, Any]]:  # delete a page
        """
                Delete a page with page_id

                Parameters
                ----------
                page_id : str or UrlLike, optional
                    Identifier for a Notion page. ID or URL
        >>>>>>> 49c59edfb64170ef62bb6baa2fd7d986fdcdce69

                Returns
                -------
                Tuple[int, Dict[str, Any]]
                    This returns status_code and response of dictionary
        """
        page_id = self._parse_id(page_id, type_="page")  # parse ID from URL

        # set body
        body = {
            "archived": True,
        }
        # delete a page
        res = requests.patch(
            f"https://api.notion.com/v1/pages/{page_id}",
            headers=self.headers,
            data=json.dumps(body),
        )

        return res.status_code, res.json()

    # Blocks
    def get_block(
        self,
        *,
        block_id: Union[str, UrlLike],
    ) -> Tuple[int, Dict[str, Any]]:
        """
        Get a block with block_id

        Parameters
        ----------
        block_id : str or UrlLike
            Identifier for a Notion block. ID or URL

        Returns
        -------
        Tuple[int, Dict[str, Any]]
            This returns status_code and response of dictionary
        """
        block_id = self._parse_id(block_id, type_="block")
        res = requests.get(
            f"https://api.notion.com/v1/blocks/{block_id}", headers=self.headers
        )
        return res.status_code, res.json()

    def update_block(
        self,
        *,
        block_id: Union[str, UrlLike],
        type_: Optional[Dict] = None,
        archived: bool = False,
    ) -> Tuple[int, Dict[str, Any]]:
        """
        Updates the content for the specified block_id based on the block type.
        Supported fields based on the block object type
        (see [Block object](https://developers.notion.com/reference-link/block#block-type-object) for available fields
        and the expected input for each field)

        Parameters
        ----------
        block_id : str or UrlLike
            Identifier for a Notion block. ID or URL
        type_ : Dict, optional
            The block object type value with the properties to be updated.
            Currently only `text` (for supported block types) and `checked` (for to_do blocks) fields can be updated
        archived : bool, default=False
            Set to true to archive (delete) a block. Set to false to un-archive (restore) a block

        Returns
        -------
        Tuple[int, Dict[str, Any]]
            This returns status_code and response of dictionary

        See Also
        --------
        [Block object](https://developers.notion.com/reference-link/block#block-type-object)

        .. note:: A block's children CANNOT be directly updated with this endpoint.
                    Instead use `append_block_children` to add children
        """
        block_id = self._parse_id(block_id, type_="block")
        body = {}
        if type_ is not None:
            body.update(type_)
        body.update(
            {
                "archived": archived,
            }
        )

        res = requests.patch(
            f"https://api.notion.com/v1/blocks/{block_id}",
            headers=self.headers,
            data=json.dumps(body),
        )
        return res.status_code, res.json()

    def get_block_children(
        self,
        *,
        block_id: Union[str, UrlLike],
        start_cursor: Optional[str] = None,
        page_size: int = 100,
    ) -> Tuple[int, Dict[str, Any]]:
        """
        Get child blocks with block_id

        Parameters
        ----------
        block_id : str or UrlLike
            Identifier for a block. ID or URL
        start_cursor : str, optional
            If supplied, this endpoint will return a page of results starting after the cursor provided.
            If not supplied, this endpoint will return the first page of results
        page_size : int, default=100
            The number of items from the full list desired in the response. Maximum: 100

        Returns
        -------
        Tuple[int, Dict[str, Any]]
            This returns status_code and response of dictionary

        Raises
        ------
        ValueError
            if page_size is 0 or less than 0
        """
        if page_size <= 0:  # 1 <= page_size <= 100
            raise ValueError("page_size must be more than 0")
        elif page_size > 100:  # 1 <= page_size <= 100
            page_size = 100
            warnings.warn(
                "page_size must be up to 100, page_size is set to 100", UserWarning
            )

        block_id = self._parse_id(
            block_id, type_="block"
        )  # parse block_id from url-like
        body = {
            "page_size": page_size,  # max size of page_size
            "start_cursor": start_cursor,  # start_cursor
        }
        res = requests.get(
            f"https://api.notion.com/v1/blocks/{block_id}/children",
            headers=self.headers,
            params=body,
        )
        return res.status_code, res.json()

    def append_block_children(
        self,
        *,
        block_id: Union[str, UrlLike],
        children: Children,
    ) -> Tuple[int, Dict[str, Any]]:
        """
        Creates and appends new children blocks to the parent block_id specified.
        Returns a paginated list of newly created first level children block objects.

        Parameters
        ----------
        block_id : str or UrlLike
            Identifier for a block. ID or URL
        children : list of Any
            Child content to append to a container block as an array of block objects

        Returns
        -------
        Tuple[int, Dict[str, Any]]
            This returns status_code and response of dictionary

        Raises
        ------
        ValueError
            if page_size is 0 or less than 0

        Usage
        -----
        >>> from notion_extensions.base.props.block.children import Children
        >>> heading = Heading1(text)
        >>> children = Children(heading)
        >>> client.append_block_children(block_id="https://", children=children)
        """
        # parse block_id from url-like
        block_id = self._parse_id(block_id, type_="block")

        res = requests.patch(
            f"https://api.notion.com/v1/blocks/{block_id}/children",
            headers=self.headers,
            data=json.dumps(children),
        )
        return res.status_code, res.json()

    def delete_block(
        self, *, block_id: Union[str, UrlLike]
    ) -> Tuple[int, Dict[str, Any]]:
        """
        Sets a Block object, including page blocks, to archived: true using the ID or URL specified.
        To restore the block with the API, use `update_block` or `update_page` respectively.

        Parameters
        ----------
        block_id : str or UrlLike
            Identifier for a Notion block. ID or URL

        Returns
        -------
        Tuple[int, Dict[str, Any]]
            This returns status_code and response of dictionary
        """
        block_id = self._parse_id(block_id, type_="block")
        res = requests.delete(
            f"https://api.notion.com/v1/blocks/{block_id}", headers=self.headers
        )
        return res.status_code, res.json()
