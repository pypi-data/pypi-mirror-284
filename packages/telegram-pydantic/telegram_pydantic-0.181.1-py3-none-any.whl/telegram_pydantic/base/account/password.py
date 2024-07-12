from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# account.Password - Layer 181
Password = typing.Annotated[
    typing.Union[
        types.account.Password
    ],
    pydantic.Field(discriminator='QUALNAME')
]
