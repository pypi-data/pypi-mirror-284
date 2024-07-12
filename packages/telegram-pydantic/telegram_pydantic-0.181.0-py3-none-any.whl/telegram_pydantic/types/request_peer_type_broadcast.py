from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class RequestPeerTypeBroadcast(BaseModel):
    """
    types.RequestPeerTypeBroadcast
    ID: 0x339bef6c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.RequestPeerTypeBroadcast'] = pydantic.Field(
        'types.RequestPeerTypeBroadcast',
        alias='_'
    )

    creator: typing.Optional[bool] = None
    has_username: typing.Optional[bool] = None
    user_admin_rights: typing.Optional["base.ChatAdminRights"] = None
    bot_admin_rights: typing.Optional["base.ChatAdminRights"] = None
