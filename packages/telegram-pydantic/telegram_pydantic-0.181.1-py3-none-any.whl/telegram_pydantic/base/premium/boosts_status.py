from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# premium.BoostsStatus - Layer 181
BoostsStatus = typing.Annotated[
    typing.Union[
        types.premium.BoostsStatus
    ],
    pydantic.Field(discriminator='QUALNAME')
]
