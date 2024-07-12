from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# contacts.ContactBirthdays - Layer 181
ContactBirthdays = typing.Annotated[
    typing.Union[
        types.contacts.ContactBirthdays
    ],
    pydantic.Field(discriminator='QUALNAME')
]
