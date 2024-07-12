from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ClearAllDrafts(BaseModel):
    """
    functions.messages.ClearAllDrafts
    ID: 0x7e58ee9c
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.ClearAllDrafts'] = pydantic.Field(
        'functions.messages.ClearAllDrafts',
        alias='_'
    )

