from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# contacts.ImportedContacts - Layer 181
ImportedContacts = typing.Annotated[
    typing.Union[
        types.contacts.ImportedContacts
    ],
    pydantic.Field(discriminator='QUALNAME')
]
