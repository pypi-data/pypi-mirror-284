from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# BankCardOpenUrl - Layer 181
BankCardOpenUrl = typing.Annotated[
    typing.Union[
        types.BankCardOpenUrl
    ],
    pydantic.Field(discriminator='QUALNAME')
]
