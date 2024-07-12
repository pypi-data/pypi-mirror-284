from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# StarsTransaction - Layer 181
StarsTransaction = typing.Annotated[
    typing.Union[
        types.StarsTransaction
    ],
    pydantic.Field(discriminator='QUALNAME')
]
