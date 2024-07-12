from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionPinTopic(BaseModel):
    """
    types.ChannelAdminLogEventActionPinTopic
    ID: 0x5d8d353b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionPinTopic'] = pydantic.Field(
        'types.ChannelAdminLogEventActionPinTopic',
        alias='_'
    )

    prev_topic: typing.Optional["base.ForumTopic"] = None
    new_topic: typing.Optional["base.ForumTopic"] = None
