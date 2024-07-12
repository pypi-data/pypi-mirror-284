from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# stats.PublicForwards - Layer 181
PublicForwards = typing.Annotated[
    typing.Union[
        types.stats.PublicForwards
    ],
    pydantic.Field(discriminator='QUALNAME')
]
