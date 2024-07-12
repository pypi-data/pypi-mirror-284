from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# help.PromoData - Layer 181
PromoData = typing.Annotated[
    typing.Union[
        types.help.PromoData,
        types.help.PromoDataEmpty
    ],
    pydantic.Field(discriminator='QUALNAME')
]
