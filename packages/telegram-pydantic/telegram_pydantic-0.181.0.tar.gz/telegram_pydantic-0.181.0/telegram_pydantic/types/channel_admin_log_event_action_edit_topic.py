from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionEditTopic(BaseModel):
    """
    types.ChannelAdminLogEventActionEditTopic
    ID: 0xf06fe208
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionEditTopic'] = pydantic.Field(
        'types.ChannelAdminLogEventActionEditTopic',
        alias='_'
    )

    prev_topic: "base.ForumTopic"
    new_topic: "base.ForumTopic"
