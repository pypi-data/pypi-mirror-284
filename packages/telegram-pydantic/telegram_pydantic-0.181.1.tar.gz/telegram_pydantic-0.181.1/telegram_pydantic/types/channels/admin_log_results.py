from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AdminLogResults(BaseModel):
    """
    types.channels.AdminLogResults
    ID: 0xed8af74d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.channels.AdminLogResults'] = pydantic.Field(
        'types.channels.AdminLogResults',
        alias='_'
    )

    events: list["base.ChannelAdminLogEvent"]
    chats: list["base.Chat"]
    users: list["base.User"]
