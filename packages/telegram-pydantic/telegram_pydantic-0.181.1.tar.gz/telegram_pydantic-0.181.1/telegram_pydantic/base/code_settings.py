from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# CodeSettings - Layer 181
CodeSettings = typing.Annotated[
    typing.Union[
        types.CodeSettings
    ],
    pydantic.Field(discriminator='QUALNAME')
]
