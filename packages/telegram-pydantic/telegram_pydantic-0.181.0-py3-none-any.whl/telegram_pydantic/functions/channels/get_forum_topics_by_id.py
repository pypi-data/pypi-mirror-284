from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetForumTopicsByID(BaseModel):
    """
    functions.channels.GetForumTopicsByID
    ID: 0xb0831eb9
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.GetForumTopicsByID'] = pydantic.Field(
        'functions.channels.GetForumTopicsByID',
        alias='_'
    )

    channel: "base.InputChannel"
    topics: list[int]
