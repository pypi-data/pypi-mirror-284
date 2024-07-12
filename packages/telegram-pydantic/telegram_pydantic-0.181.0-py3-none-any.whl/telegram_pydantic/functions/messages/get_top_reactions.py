from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetTopReactions(BaseModel):
    """
    functions.messages.GetTopReactions
    ID: 0xbb8125ba
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetTopReactions'] = pydantic.Field(
        'functions.messages.GetTopReactions',
        alias='_'
    )

    limit: int
    hash: int
