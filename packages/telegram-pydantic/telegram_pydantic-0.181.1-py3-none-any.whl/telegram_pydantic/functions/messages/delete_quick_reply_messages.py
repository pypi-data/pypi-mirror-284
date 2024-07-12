from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DeleteQuickReplyMessages(BaseModel):
    """
    functions.messages.DeleteQuickReplyMessages
    ID: 0xe105e910
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.DeleteQuickReplyMessages'] = pydantic.Field(
        'functions.messages.DeleteQuickReplyMessages',
        alias='_'
    )

    shortcut_id: int
    id: list[int]
