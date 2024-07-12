from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# premium.BoostsList - Layer 181
BoostsList = typing.Annotated[
    typing.Union[
        types.premium.BoostsList
    ],
    pydantic.Field(discriminator='QUALNAME')
]
