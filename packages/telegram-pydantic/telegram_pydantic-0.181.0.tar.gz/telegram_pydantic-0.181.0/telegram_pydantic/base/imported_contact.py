from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# ImportedContact - Layer 181
ImportedContact = typing.Annotated[
    typing.Union[
        types.ImportedContact
    ],
    pydantic.Field(discriminator='QUALNAME')
]
