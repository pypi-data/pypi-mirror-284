from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateFolderPeers(BaseModel):
    """
    types.UpdateFolderPeers
    ID: 0x19360dc0
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateFolderPeers'] = pydantic.Field(
        'types.UpdateFolderPeers',
        alias='_'
    )

    folder_peers: list["base.FolderPeer"]
    pts: int
    pts_count: int
