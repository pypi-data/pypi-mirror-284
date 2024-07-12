from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Chat(BaseModel):
    """
    types.Chat
    ID: 0x41cbf256
    Layer: 181
    """
    QUALNAME: typing.Literal['types.Chat'] = pydantic.Field(
        'types.Chat',
        alias='_'
    )

    id: int
    title: str
    photo: "base.ChatPhoto"
    participants_count: int
    date: int
    version: int
    creator: typing.Optional[bool] = None
    left: typing.Optional[bool] = None
    deactivated: typing.Optional[bool] = None
    call_active: typing.Optional[bool] = None
    call_not_empty: typing.Optional[bool] = None
    noforwards: typing.Optional[bool] = None
    migrated_to: typing.Optional["base.InputChannel"] = None
    admin_rights: typing.Optional["base.ChatAdminRights"] = None
    default_banned_rights: typing.Optional["base.ChatBannedRights"] = None
