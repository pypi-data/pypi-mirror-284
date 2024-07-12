from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionSendMessage(BaseModel):
    """
    types.ChannelAdminLogEventActionSendMessage
    ID: 0x278f2868
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionSendMessage'] = pydantic.Field(
        'types.ChannelAdminLogEventActionSendMessage',
        alias='_'
    )

    message: "base.Message"
