from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Contacts(BaseModel):
    """
    types.contacts.Contacts
    ID: 0xeae87e42
    Layer: 181
    """
    QUALNAME: typing.Literal['types.contacts.Contacts'] = pydantic.Field(
        'types.contacts.Contacts',
        alias='_'
    )

    contacts: list["base.Contact"]
    saved_count: int
    users: list["base.User"]
