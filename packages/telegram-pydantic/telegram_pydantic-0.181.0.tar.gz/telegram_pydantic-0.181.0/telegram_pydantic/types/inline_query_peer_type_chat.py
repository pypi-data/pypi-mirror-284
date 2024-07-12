from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InlineQueryPeerTypeChat(BaseModel):
    """
    types.InlineQueryPeerTypeChat
    ID: 0xd766c50a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InlineQueryPeerTypeChat'] = pydantic.Field(
        'types.InlineQueryPeerTypeChat',
        alias='_'
    )

