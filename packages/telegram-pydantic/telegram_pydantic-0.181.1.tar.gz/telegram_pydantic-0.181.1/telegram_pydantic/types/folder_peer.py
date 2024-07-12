from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class FolderPeer(BaseModel):
    """
    types.FolderPeer
    ID: 0xe9baa668
    Layer: 181
    """
    QUALNAME: typing.Literal['types.FolderPeer'] = pydantic.Field(
        'types.FolderPeer',
        alias='_'
    )

    peer: "base.Peer"
    folder_id: int
