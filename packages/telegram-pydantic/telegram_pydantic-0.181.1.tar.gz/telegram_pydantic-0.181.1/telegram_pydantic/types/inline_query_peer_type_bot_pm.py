from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InlineQueryPeerTypeBotPM(BaseModel):
    """
    types.InlineQueryPeerTypeBotPM
    ID: 0xe3b2d0c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InlineQueryPeerTypeBotPM'] = pydantic.Field(
        'types.InlineQueryPeerTypeBotPM',
        alias='_'
    )

