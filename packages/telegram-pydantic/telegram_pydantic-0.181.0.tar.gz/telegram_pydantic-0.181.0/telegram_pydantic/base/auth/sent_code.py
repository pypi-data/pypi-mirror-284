from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# auth.SentCode - Layer 181
SentCode = typing.Annotated[
    typing.Union[
        types.auth.SentCode,
        types.auth.SentCodeSuccess
    ],
    pydantic.Field(discriminator='QUALNAME')
]
