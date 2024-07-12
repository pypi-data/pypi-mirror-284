from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputUser - Layer 181
InputUser = typing.Annotated[
    typing.Union[
        types.InputUser,
        types.InputUserEmpty,
        types.InputUserFromMessage,
        types.InputUserSelf
    ],
    pydantic.Field(discriminator='QUALNAME')
]
