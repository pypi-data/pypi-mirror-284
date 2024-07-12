from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputContact - Layer 181
InputContact = typing.Annotated[
    typing.Union[
        types.InputPhoneContact
    ],
    pydantic.Field(discriminator='QUALNAME')
]
