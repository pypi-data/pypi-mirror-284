from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# AccountDaysTTL - Layer 181
AccountDaysTTL = typing.Annotated[
    typing.Union[
        types.AccountDaysTTL
    ],
    pydantic.Field(discriminator='QUALNAME')
]
