from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# User - Layer 181
User = typing.Annotated[
    typing.Union[
        types.User,
        types.UserEmpty
    ],
    pydantic.Field(discriminator='QUALNAME')
]
