from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateBotInlineQuery(BaseModel):
    """
    types.UpdateBotInlineQuery
    ID: 0x496f379c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateBotInlineQuery'] = pydantic.Field(
        'types.UpdateBotInlineQuery',
        alias='_'
    )

    query_id: int
    user_id: int
    query: str
    offset: str
    geo: typing.Optional["base.GeoPoint"] = None
    peer_type: typing.Optional["base.InlineQueryPeerType"] = None
