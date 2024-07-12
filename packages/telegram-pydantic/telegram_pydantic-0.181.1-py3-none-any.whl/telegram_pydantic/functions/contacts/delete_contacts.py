from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DeleteContacts(BaseModel):
    """
    functions.contacts.DeleteContacts
    ID: 0x96a0e00
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.contacts.DeleteContacts'] = pydantic.Field(
        'functions.contacts.DeleteContacts',
        alias='_'
    )

    id: list["base.InputUser"]
