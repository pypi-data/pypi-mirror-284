from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageRange(BaseModel):
    """
    types.MessageRange
    ID: 0xae30253
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageRange'] = pydantic.Field(
        'types.MessageRange',
        alias='_'
    )

    min_id: int
    max_id: int
