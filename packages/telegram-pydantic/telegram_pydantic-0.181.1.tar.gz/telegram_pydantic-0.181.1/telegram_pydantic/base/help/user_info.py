from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# help.UserInfo - Layer 181
UserInfo = typing.Annotated[
    typing.Union[
        types.help.UserInfo,
        types.help.UserInfoEmpty
    ],
    pydantic.Field(discriminator='QUALNAME')
]
