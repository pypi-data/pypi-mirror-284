from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionDeleteTopic(BaseModel):
    """
    types.ChannelAdminLogEventActionDeleteTopic
    ID: 0xae168909
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionDeleteTopic'] = pydantic.Field(
        'types.ChannelAdminLogEventActionDeleteTopic',
        alias='_'
    )

    topic: "base.ForumTopic"
