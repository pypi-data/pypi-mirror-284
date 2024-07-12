from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReorderQuickReplies(BaseModel):
    """
    functions.messages.ReorderQuickReplies
    ID: 0x60331907
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.ReorderQuickReplies'] = pydantic.Field(
        'functions.messages.ReorderQuickReplies',
        alias='_'
    )

    order: list[int]
