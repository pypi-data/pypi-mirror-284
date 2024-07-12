from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# account.SentEmailCode - Layer 181
SentEmailCode = typing.Annotated[
    typing.Union[
        types.account.SentEmailCode
    ],
    pydantic.Field(discriminator='QUALNAME')
]
