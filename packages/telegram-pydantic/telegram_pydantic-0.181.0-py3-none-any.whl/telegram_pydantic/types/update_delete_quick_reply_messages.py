from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateDeleteQuickReplyMessages(BaseModel):
    """
    types.UpdateDeleteQuickReplyMessages
    ID: 0x566fe7cd
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateDeleteQuickReplyMessages'] = pydantic.Field(
        'types.UpdateDeleteQuickReplyMessages',
        alias='_'
    )

    shortcut_id: int
    messages: list[int]
