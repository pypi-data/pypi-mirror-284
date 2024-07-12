from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionExportedInviteEdit(BaseModel):
    """
    types.ChannelAdminLogEventActionExportedInviteEdit
    ID: 0xe90ebb59
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionExportedInviteEdit'] = pydantic.Field(
        'types.ChannelAdminLogEventActionExportedInviteEdit',
        alias='_'
    )

    prev_invite: "base.ExportedChatInvite"
    new_invite: "base.ExportedChatInvite"
