from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DefaultHistoryTTL(BaseModel):
    """
    types.DefaultHistoryTTL
    ID: 0x43b46b20
    Layer: 181
    """
    QUALNAME: typing.Literal['types.DefaultHistoryTTL'] = pydantic.Field(
        'types.DefaultHistoryTTL',
        alias='_'
    )

    period: int
