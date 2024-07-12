from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionEditMessage(BaseModel):
    """
    types.ChannelAdminLogEventActionEditMessage
    ID: 0x709b2405
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionEditMessage'] = pydantic.Field(
        'types.ChannelAdminLogEventActionEditMessage',
        alias='_'
    )

    prev_message: "base.Message"
    new_message: "base.Message"
