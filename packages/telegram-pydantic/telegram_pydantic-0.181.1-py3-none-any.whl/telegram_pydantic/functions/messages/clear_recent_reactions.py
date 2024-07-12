from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ClearRecentReactions(BaseModel):
    """
    functions.messages.ClearRecentReactions
    ID: 0x9dfeefb4
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.ClearRecentReactions'] = pydantic.Field(
        'functions.messages.ClearRecentReactions',
        alias='_'
    )

