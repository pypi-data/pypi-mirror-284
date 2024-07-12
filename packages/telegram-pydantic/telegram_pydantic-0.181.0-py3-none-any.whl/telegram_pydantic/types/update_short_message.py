from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateShortMessage(BaseModel):
    """
    types.UpdateShortMessage
    ID: 0x313bc7f8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateShortMessage'] = pydantic.Field(
        'types.UpdateShortMessage',
        alias='_'
    )

    id: int
    user_id: int
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
