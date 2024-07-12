from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class RequestPeerTypeChat(BaseModel):
    """
    types.RequestPeerTypeChat
    ID: 0xc9f06e1b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.RequestPeerTypeChat'] = pydantic.Field(
        'types.RequestPeerTypeChat',
        alias='_'
    )

    creator: typing.Optional[bool] = None
    bot_participant: typing.Optional[bool] = None
    has_username: typing.Optional[bool] = None
    forum: typing.Optional[bool] = None
    user_admin_rights: typing.Optional["base.ChatAdminRights"] = None
    bot_admin_rights: typing.Optional["base.ChatAdminRights"] = None
