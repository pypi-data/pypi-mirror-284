from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# account.PasswordSettings - Layer 181
PasswordSettings = typing.Annotated[
    typing.Union[
        types.account.PasswordSettings
    ],
    pydantic.Field(discriminator='QUALNAME')
]
