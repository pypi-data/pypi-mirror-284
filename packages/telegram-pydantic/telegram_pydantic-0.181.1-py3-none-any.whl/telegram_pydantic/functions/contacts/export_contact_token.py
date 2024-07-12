from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ExportContactToken(BaseModel):
    """
    functions.contacts.ExportContactToken
    ID: 0xf8654027
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.contacts.ExportContactToken'] = pydantic.Field(
        'functions.contacts.ExportContactToken',
        alias='_'
    )

