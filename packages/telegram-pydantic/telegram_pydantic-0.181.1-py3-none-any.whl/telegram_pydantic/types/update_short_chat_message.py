from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateShortChatMessage(BaseModel):
    """
    types.UpdateShortChatMessage
    ID: 0x4d6deea5
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateShortChatMessage'] = pydantic.Field(
        'types.UpdateShortChatMessage',
        alias='_'
    )

    id: int
    from_id: int
    chat_id: int
    message: str
    pts: int
    pts_count: int
    date: int
    out: typing.Optional[bool] = None
    mentioned: typing.Optional[bool] = None
    media_unread: typing.Optional[bool] = None
    silent: typing.Optional[bool] = None
    fwd_from: typing.Optional["base.MessageFwdHeader"] = None
    via_bot_id: typing.Optional[int] = None
    reply_to: typing.Optional["base.MessageReplyHeader"] = None
    entities: typing.Optional[list["base.MessageEntity"]] = None
    ttl_period: typing.Optional[int] = None
