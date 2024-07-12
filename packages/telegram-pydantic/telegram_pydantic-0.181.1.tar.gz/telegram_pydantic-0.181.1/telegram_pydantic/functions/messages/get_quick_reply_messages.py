from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetQuickReplyMessages(BaseModel):
    """
    functions.messages.GetQuickReplyMessages
    ID: 0x94a495c3
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetQuickReplyMessages'] = pydantic.Field(
        'functions.messages.GetQuickReplyMessages',
        alias='_'
    )

    shortcut_id: int
    hash: int
    id: typing.Optional[list[int]] = None
