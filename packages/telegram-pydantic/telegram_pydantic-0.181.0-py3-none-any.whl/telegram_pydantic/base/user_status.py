from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# UserStatus - Layer 181
UserStatus = typing.Annotated[
    typing.Union[
        types.UserStatusEmpty,
        types.UserStatusLastMonth,
        types.UserStatusLastWeek,
        types.UserStatusOffline,
        types.UserStatusOnline,
        types.UserStatusRecently
    ],
    pydantic.Field(discriminator='QUALNAME')
]
