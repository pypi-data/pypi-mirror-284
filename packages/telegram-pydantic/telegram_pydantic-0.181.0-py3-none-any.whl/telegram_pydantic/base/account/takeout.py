from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# account.Takeout - Layer 181
Takeout = typing.Annotated[
    typing.Union[
        types.account.Takeout
    ],
    pydantic.Field(discriminator='QUALNAME')
]
