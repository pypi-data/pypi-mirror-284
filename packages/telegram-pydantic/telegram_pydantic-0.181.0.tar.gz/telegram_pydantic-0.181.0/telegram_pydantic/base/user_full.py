from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# UserFull - Layer 181
UserFull = typing.Annotated[
    typing.Union[
        types.UserFull
    ],
    pydantic.Field(discriminator='QUALNAME')
]
