from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# contacts.Contacts - Layer 181
Contacts = typing.Annotated[
    typing.Union[
        types.contacts.Contacts,
        types.contacts.ContactsNotModified
    ],
    pydantic.Field(discriminator='QUALNAME')
]
