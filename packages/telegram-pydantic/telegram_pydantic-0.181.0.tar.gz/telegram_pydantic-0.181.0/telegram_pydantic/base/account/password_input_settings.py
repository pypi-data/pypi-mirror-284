from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# account.PasswordInputSettings - Layer 181
PasswordInputSettings = typing.Annotated[
    typing.Union[
        types.account.PasswordInputSettings
    ],
    pydantic.Field(discriminator='QUALNAME')
]
