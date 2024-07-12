from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# contacts.Found - Layer 181
Found = typing.Annotated[
    typing.Union[
        types.contacts.Found
    ],
    pydantic.Field(discriminator='QUALNAME')
]
