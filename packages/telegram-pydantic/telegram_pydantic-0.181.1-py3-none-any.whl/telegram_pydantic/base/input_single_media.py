from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputSingleMedia - Layer 181
InputSingleMedia = typing.Annotated[
    typing.Union[
        types.InputSingleMedia
    ],
    pydantic.Field(discriminator='QUALNAME')
]
