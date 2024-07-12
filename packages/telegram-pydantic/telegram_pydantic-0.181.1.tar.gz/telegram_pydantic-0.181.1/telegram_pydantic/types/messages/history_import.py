from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class HistoryImport(BaseModel):
    """
    types.messages.HistoryImport
    ID: 0x1662af0b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.HistoryImport'] = pydantic.Field(
        'types.messages.HistoryImport',
        alias='_'
    )

    id: int
