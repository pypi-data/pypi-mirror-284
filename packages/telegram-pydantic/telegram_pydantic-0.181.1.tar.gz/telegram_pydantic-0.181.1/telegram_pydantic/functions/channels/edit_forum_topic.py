from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EditForumTopic(BaseModel):
    """
    functions.channels.EditForumTopic
    ID: 0xf4dfa185
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.EditForumTopic'] = pydantic.Field(
        'functions.channels.EditForumTopic',
        alias='_'
    )

    channel: "base.InputChannel"
    topic_id: int
    title: typing.Optional[str] = None
    icon_emoji_id: typing.Optional[int] = None
    closed: typing.Optional[bool] = None
    hidden: typing.Optional[bool] = None
