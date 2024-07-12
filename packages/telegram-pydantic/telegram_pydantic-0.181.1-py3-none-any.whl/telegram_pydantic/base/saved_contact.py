from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# SavedContact - Layer 181
SavedContact = typing.Annotated[
    typing.Union[
        types.SavedPhoneContact
    ],
    pydantic.Field(discriminator='QUALNAME')
]
