from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ResetSaved(BaseModel):
    """
    functions.contacts.ResetSaved
    ID: 0x879537f1
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.contacts.ResetSaved'] = pydantic.Field(
        'functions.contacts.ResetSaved',
        alias='_'
    )

