from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetContacts(BaseModel):
    """
    functions.contacts.GetContacts
    ID: 0x5dd69e12
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.contacts.GetContacts'] = pydantic.Field(
        'functions.contacts.GetContacts',
        alias='_'
    )

    hash: int
