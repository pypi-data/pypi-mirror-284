from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetQuickReplies(BaseModel):
    """
    functions.messages.GetQuickReplies
    ID: 0xd483f2a8
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetQuickReplies'] = pydantic.Field(
        'functions.messages.GetQuickReplies',
        alias='_'
    )

    hash: int
