from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ContactsNotModified(BaseModel):
    """
    types.contacts.ContactsNotModified
    ID: 0xb74ba9d2
    Layer: 181
    """
    QUALNAME: typing.Literal['types.contacts.ContactsNotModified'] = pydantic.Field(
        'types.contacts.ContactsNotModified',
        alias='_'
    )

