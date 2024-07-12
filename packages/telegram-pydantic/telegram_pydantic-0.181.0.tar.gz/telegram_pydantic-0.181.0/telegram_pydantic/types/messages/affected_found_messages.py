from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AffectedFoundMessages(BaseModel):
    """
    types.messages.AffectedFoundMessages
    ID: 0xef8d3e6c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.AffectedFoundMessages'] = pydantic.Field(
        'types.messages.AffectedFoundMessages',
        alias='_'
    )

    pts: int
    pts_count: int
    offset: int
    messages: list[int]
