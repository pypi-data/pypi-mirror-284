from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PostInteractionCountersMessage(BaseModel):
    """
    types.PostInteractionCountersMessage
    ID: 0xe7058e7f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PostInteractionCountersMessage'] = pydantic.Field(
        'types.PostInteractionCountersMessage',
        alias='_'
    )

    msg_id: int
    views: int
    forwards: int
    reactions: int
