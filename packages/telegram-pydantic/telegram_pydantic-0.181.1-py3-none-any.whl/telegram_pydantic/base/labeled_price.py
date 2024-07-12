from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# LabeledPrice - Layer 181
LabeledPrice = typing.Annotated[
    typing.Union[
        types.LabeledPrice
    ],
    pydantic.Field(discriminator='QUALNAME')
]
