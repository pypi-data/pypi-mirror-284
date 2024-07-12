from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# users.UserFull - Layer 181
UserFull = typing.Annotated[
    typing.Union[
        types.users.UserFull
    ],
    pydantic.Field(discriminator='QUALNAME')
]
