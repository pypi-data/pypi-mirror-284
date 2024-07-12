from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateChannelPinnedTopic(BaseModel):
    """
    types.UpdateChannelPinnedTopic
    ID: 0x192efbe3
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateChannelPinnedTopic'] = pydantic.Field(
        'types.UpdateChannelPinnedTopic',
        alias='_'
    )

    channel_id: int
    topic_id: int
    pinned: typing.Optional[bool] = None
