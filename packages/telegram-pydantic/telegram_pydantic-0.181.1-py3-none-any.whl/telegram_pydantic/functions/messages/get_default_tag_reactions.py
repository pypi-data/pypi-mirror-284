from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetDefaultTagReactions(BaseModel):
    """
    functions.messages.GetDefaultTagReactions
    ID: 0xbdf93428
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetDefaultTagReactions'] = pydantic.Field(
        'functions.messages.GetDefaultTagReactions',
        alias='_'
    )

    hash: int
