from typing import Dict, Union

from .block import Block

__all__ = [
    "Embed",
    "EMBED_PLATFORMS",
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
