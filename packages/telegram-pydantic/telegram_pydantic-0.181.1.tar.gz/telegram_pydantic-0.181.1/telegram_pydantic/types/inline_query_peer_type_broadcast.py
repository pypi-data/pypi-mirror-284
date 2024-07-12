from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InlineQueryPeerTypeBroadcast(BaseModel):
    """
    types.InlineQueryPeerTypeBroadcast
    ID: 0x6334ee9a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InlineQueryPeerTypeBroadcast'] = pydantic.Field(
        'types.InlineQueryPeerTypeBroadcast',
        alias='_'
    )

