from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateMessagePoll(BaseModel):
    """
    types.UpdateMessagePoll
    ID: 0xaca1657b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateMessagePoll'] = pydantic.Field(
        'types.UpdateMessagePoll',
        alias='_'
    )

    poll_id: int
    results: "base.PollResults"
    poll: typing.Optional["base.Poll"] = None
