from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionExportedInviteDelete(BaseModel):
    """
    types.ChannelAdminLogEventActionExportedInviteDelete
    ID: 0x5a50fca4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionExportedInviteDelete'] = pydantic.Field(
        'types.ChannelAdminLogEventActionExportedInviteDelete',
        alias='_'
    )

    invite: "base.ExportedChatInvite"
