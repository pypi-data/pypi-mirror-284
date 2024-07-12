from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# stats.MegagroupStats - Layer 181
MegagroupStats = typing.Annotated[
    typing.Union[
        types.stats.MegagroupStats
    ],
    pydantic.Field(discriminator='QUALNAME')
]
