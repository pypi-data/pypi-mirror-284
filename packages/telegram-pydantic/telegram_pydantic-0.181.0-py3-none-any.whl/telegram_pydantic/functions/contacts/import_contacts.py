from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ImportContacts(BaseModel):
    """
    functions.contacts.ImportContacts
    ID: 0x2c800be5
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.contacts.ImportContacts'] = pydantic.Field(
        'functions.contacts.ImportContacts',
        alias='_'
    )

    contacts: list["base.InputContact"]
