from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# DefaultHistoryTTL - Layer 181
DefaultHistoryTTL = typing.Annotated[
    typing.Union[
        types.DefaultHistoryTTL
    ],
    pydantic.Field(discriminator='QUALNAME')
]
