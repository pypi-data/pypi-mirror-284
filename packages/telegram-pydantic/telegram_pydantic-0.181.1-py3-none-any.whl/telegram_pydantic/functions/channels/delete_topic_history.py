from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DeleteTopicHistory(BaseModel):
    """
    functions.channels.DeleteTopicHistory
    ID: 0x34435f2d
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.DeleteTopicHistory'] = pydantic.Field(
        'functions.channels.DeleteTopicHistory',
        alias='_'
    )

    channel: "base.InputChannel"
    top_msg_id: int
