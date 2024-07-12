from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class HistoryImportParsed(BaseModel):
    """
    types.messages.HistoryImportParsed
    ID: 0x5e0fb7b9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.HistoryImportParsed'] = pydantic.Field(
        'types.messages.HistoryImportParsed',
        alias='_'
    )

    pm: typing.Optional[bool] = None
    group: typing.Optional[bool] = None
    title: typing.Optional[str] = None
