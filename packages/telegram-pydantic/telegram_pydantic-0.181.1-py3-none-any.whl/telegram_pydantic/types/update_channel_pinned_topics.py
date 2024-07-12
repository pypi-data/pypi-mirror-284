from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateChannelPinnedTopics(BaseModel):
    """
    types.UpdateChannelPinnedTopics
    ID: 0xfe198602
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateChannelPinnedTopics'] = pydantic.Field(
        'types.UpdateChannelPinnedTopics',
        alias='_'
    )

    channel_id: int
    order: typing.Optional[list[int]] = None
