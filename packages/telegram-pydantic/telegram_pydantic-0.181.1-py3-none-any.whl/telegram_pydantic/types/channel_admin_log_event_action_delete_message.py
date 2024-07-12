from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionDeleteMessage(BaseModel):
    """
    types.ChannelAdminLogEventActionDeleteMessage
    ID: 0x42e047bb
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionDeleteMessage'] = pydantic.Field(
        'types.ChannelAdminLogEventActionDeleteMessage',
        alias='_'
    )

    message: "base.Message"
