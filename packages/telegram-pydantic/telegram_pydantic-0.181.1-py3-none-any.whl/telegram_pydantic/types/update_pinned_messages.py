from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdatePinnedMessages(BaseModel):
    """
    types.UpdatePinnedMessages
    ID: 0xed85eab5
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdatePinnedMessages'] = pydantic.Field(
        'types.UpdatePinnedMessages',
        alias='_'
    )

    peer: "base.Peer"
    messages: list[int]
    pts: int
    pts_count: int
    pinned: typing.Optional[bool] = None
