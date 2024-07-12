from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# Bool - Layer 181
Bool = typing.Annotated[
    typing.Union[
        types.BoolFalse,
        types.BoolTrue
    ],
    pydantic.Field(discriminator='QUALNAME')
]
