from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionChangeLinkedChat(BaseModel):
    """
    types.ChannelAdminLogEventActionChangeLinkedChat
    ID: 0x50c7ac8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionChangeLinkedChat'] = pydantic.Field(
        'types.ChannelAdminLogEventActionChangeLinkedChat',
        alias='_'
    )

    prev_value: int
    new_value: int
