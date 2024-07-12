from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# JSONObjectValue - Layer 181
JSONObjectValue = typing.Annotated[
    typing.Union[
        types.JsonObjectValue
    ],
    pydantic.Field(discriminator='QUALNAME')
]
