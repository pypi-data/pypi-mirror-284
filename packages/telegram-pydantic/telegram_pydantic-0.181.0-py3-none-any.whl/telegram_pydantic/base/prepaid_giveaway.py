from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# PrepaidGiveaway - Layer 181
PrepaidGiveaway = typing.Annotated[
    typing.Union[
        types.PrepaidGiveaway
    ],
    pydantic.Field(discriminator='QUALNAME')
]
