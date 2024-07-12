from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetDialogFilters(BaseModel):
    """
    functions.messages.GetDialogFilters
    ID: 0xefd48c89
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetDialogFilters'] = pydantic.Field(
        'functions.messages.GetDialogFilters',
        alias='_'
    )

