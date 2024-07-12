from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# MaskCoords - Layer 181
MaskCoords = typing.Annotated[
    typing.Union[
        types.MaskCoords
    ],
    pydantic.Field(discriminator='QUALNAME')
]
