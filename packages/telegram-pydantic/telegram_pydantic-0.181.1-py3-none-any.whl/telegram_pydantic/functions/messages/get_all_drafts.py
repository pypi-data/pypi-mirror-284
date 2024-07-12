from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetAllDrafts(BaseModel):
    """
    functions.messages.GetAllDrafts
    ID: 0x6a3f8d65
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetAllDrafts'] = pydantic.Field(
        'functions.messages.GetAllDrafts',
        alias='_'
    )

