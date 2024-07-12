from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# SmsJob - Layer 181
SmsJob = typing.Annotated[
    typing.Union[
        types.SmsJob
    ],
    pydantic.Field(discriminator='QUALNAME')
]
