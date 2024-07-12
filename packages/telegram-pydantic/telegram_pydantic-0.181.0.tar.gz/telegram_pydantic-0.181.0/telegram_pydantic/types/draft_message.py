from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DraftMessage(BaseModel):
    """
    types.DraftMessage
    ID: 0x3fccf7ef
    Layer: 181
    """
    QUALNAME: typing.Literal['types.DraftMessage'] = pydantic.Field(
        'types.DraftMessage',
        alias='_'
    )

    message: str
    date: int
    no_webpage: typing.Optional[bool] = None
    invert_media: typing.Optional[bool] = None
    reply_to: typing.Optional["base.InputReplyTo"] = None
    entities: typing.Optional[list["base.MessageEntity"]] = None
    media: typing.Optional["base.InputMedia"] = None
