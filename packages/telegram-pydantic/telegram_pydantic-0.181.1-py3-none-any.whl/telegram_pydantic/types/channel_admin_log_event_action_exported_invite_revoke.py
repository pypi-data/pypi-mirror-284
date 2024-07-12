from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionExportedInviteRevoke(BaseModel):
    """
    types.ChannelAdminLogEventActionExportedInviteRevoke
    ID: 0x410a134e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionExportedInviteRevoke'] = pydantic.Field(
        'types.ChannelAdminLogEventActionExportedInviteRevoke',
        alias='_'
    )

    invite: "base.ExportedChatInvite"
