from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateDeleteScheduledMessages(BaseModel):
    """
    types.UpdateDeleteScheduledMessages
    ID: 0x90866cee
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateDeleteScheduledMessages'] = pydantic.Field(
        'types.UpdateDeleteScheduledMessages',
        alias='_'
    )

    peer: "base.Peer"
    messages: list[int]
