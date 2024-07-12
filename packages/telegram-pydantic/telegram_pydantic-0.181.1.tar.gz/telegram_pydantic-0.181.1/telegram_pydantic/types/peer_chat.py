from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PeerChat(BaseModel):
    """
    types.PeerChat
    ID: 0x36c6019a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PeerChat'] = pydantic.Field(
        'types.PeerChat',
        alias='_'
    )

    chat_id: int
