from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ImportContactToken(BaseModel):
    """
    functions.contacts.ImportContactToken
    ID: 0x13005788
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.contacts.ImportContactToken'] = pydantic.Field(
        'functions.contacts.ImportContactToken',
        alias='_'
    )

    token: str
