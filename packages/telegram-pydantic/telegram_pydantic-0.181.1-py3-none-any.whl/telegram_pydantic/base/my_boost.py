from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# MyBoost - Layer 181
MyBoost = typing.Annotated[
    typing.Union[
        types.MyBoost
    ],
    pydantic.Field(discriminator='QUALNAME')
]
