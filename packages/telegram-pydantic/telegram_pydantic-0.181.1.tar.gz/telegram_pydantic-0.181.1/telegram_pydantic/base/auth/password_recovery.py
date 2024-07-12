from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# auth.PasswordRecovery - Layer 181
PasswordRecovery = typing.Annotated[
    typing.Union[
        types.auth.PasswordRecovery
    ],
    pydantic.Field(discriminator='QUALNAME')
]
