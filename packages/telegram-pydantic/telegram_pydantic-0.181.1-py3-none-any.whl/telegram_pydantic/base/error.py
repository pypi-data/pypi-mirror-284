from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# Error - Layer 181
Error = typing.Annotated[
    typing.Union[
        types.Error
    ],
    pydantic.Field(discriminator='QUALNAME')
]
