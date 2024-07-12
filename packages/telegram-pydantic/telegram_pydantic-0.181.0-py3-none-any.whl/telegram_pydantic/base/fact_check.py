from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# FactCheck - Layer 181
FactCheck = typing.Annotated[
    typing.Union[
        types.FactCheck
    ],
    pydantic.Field(discriminator='QUALNAME')
]
