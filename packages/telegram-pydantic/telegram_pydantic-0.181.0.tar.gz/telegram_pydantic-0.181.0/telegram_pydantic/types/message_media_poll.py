from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageMediaPoll(BaseModel):
    """
    types.MessageMediaPoll
    ID: 0x4bd6e798
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageMediaPoll'] = pydantic.Field(
        'types.MessageMediaPoll',
        alias='_'
    )

    poll: "base.Poll"
    results: "base.PollResults"
