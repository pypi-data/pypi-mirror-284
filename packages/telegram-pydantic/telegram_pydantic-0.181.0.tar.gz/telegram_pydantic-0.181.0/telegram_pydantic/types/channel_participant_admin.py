from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelParticipantAdmin(BaseModel):
    """
    types.ChannelParticipantAdmin
    ID: 0x34c3bb53
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelParticipantAdmin'] = pydantic.Field(
        'types.ChannelParticipantAdmin',
        alias='_'
    )

    user_id: int
    promoted_by: int
    date: int
    admin_rights: "base.ChatAdminRights"
    can_edit: typing.Optional[bool] = None
    is_self: typing.Optional[bool] = pydantic.Field(None, alias='self')
    inviter_id: typing.Optional[int] = None
    rank: typing.Optional[str] = None
