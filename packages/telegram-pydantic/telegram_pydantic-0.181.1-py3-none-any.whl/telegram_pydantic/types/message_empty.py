from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageEmpty(BaseModel):
    """
    types.MessageEmpty
    ID: 0x90a6ca84
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageEmpty'] = pydantic.Field(
        'types.MessageEmpty',
        alias='_'
    )

    id: int
    peer_id: typing.Optional["base.Peer"] = None
