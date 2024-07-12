from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ExportedChatlistInvite(BaseModel):
    """
    types.ExportedChatlistInvite
    ID: 0xc5181ac
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ExportedChatlistInvite'] = pydantic.Field(
        'types.ExportedChatlistInvite',
        alias='_'
    )

    title: str
    url: str
    peers: list["base.Peer"]
