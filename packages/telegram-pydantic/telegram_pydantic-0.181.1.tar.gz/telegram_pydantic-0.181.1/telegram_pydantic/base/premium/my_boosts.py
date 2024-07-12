from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# premium.MyBoosts - Layer 181
MyBoosts = typing.Annotated[
    typing.Union[
        types.premium.MyBoosts
    ],
    pydantic.Field(discriminator='QUALNAME')
]
