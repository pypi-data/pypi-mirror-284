from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetAvailableReactions(BaseModel):
    """
    functions.messages.GetAvailableReactions
    ID: 0x18dea0ac
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetAvailableReactions'] = pydantic.Field(
        'functions.messages.GetAvailableReactions',
        alias='_'
    )

    hash: int
