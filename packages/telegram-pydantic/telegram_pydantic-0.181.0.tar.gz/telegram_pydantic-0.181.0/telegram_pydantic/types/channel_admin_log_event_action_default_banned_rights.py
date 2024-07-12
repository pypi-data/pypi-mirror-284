from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionDefaultBannedRights(BaseModel):
    """
    types.ChannelAdminLogEventActionDefaultBannedRights
    ID: 0x2df5fc0a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionDefaultBannedRights'] = pydantic.Field(
        'types.ChannelAdminLogEventActionDefaultBannedRights',
        alias='_'
    )

    prev_banned_rights: "base.ChatBannedRights"
    new_banned_rights: "base.ChatBannedRights"
