from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CreateForumTopic(BaseModel):
    """
    functions.channels.CreateForumTopic
    ID: 0xf40c0224
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.CreateForumTopic'] = pydantic.Field(
        'functions.channels.CreateForumTopic',
        alias='_'
    )

    channel: "base.InputChannel"
    title: str
    random_id: int
    icon_color: typing.Optional[int] = None
    icon_emoji_id: typing.Optional[int] = None
    send_as: typing.Optional["base.InputPeer"] = None
