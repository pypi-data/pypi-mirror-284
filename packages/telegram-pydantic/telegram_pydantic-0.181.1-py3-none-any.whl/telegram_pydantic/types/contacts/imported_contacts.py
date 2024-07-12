from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ImportedContacts(BaseModel):
    """
    types.contacts.ImportedContacts
    ID: 0x77d01c3b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.contacts.ImportedContacts'] = pydantic.Field(
        'types.contacts.ImportedContacts',
        alias='_'
    )

    imported: list["base.ImportedContact"]
    popular_invites: list["base.PopularContact"]
    retry_contacts: list[int]
    users: list["base.User"]
