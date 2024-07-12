from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# auth.LoginToken - Layer 181
LoginToken = typing.Annotated[
    typing.Union[
        types.auth.LoginToken,
        types.auth.LoginTokenMigrateTo,
        types.auth.LoginTokenSuccess
    ],
    pydantic.Field(discriminator='QUALNAME')
]
