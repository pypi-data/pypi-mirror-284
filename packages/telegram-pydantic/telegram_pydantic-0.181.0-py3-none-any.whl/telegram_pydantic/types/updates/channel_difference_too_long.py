from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelDifferenceTooLong(BaseModel):
    """
    types.updates.ChannelDifferenceTooLong
    ID: 0xa4bcc6fe
    Layer: 181
    """
    QUALNAME: typing.Literal['types.updates.ChannelDifferenceTooLong'] = pydantic.Field(
        'types.updates.ChannelDifferenceTooLong',
        alias='_'
    )

    dialog: "base.Dialog"
    messages: list["base.Message"]
    chats: list["base.Chat"]
    users: list["base.User"]
    final: typing.Optional[bool] = None
    timeout: typing.Optional[int] = None
