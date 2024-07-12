from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelMessagesFilterEmpty(BaseModel):
    """
    types.ChannelMessagesFilterEmpty
    ID: 0x94d42ee7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelMessagesFilterEmpty'] = pydantic.Field(
        'types.ChannelMessagesFilterEmpty',
        alias='_'
    )

