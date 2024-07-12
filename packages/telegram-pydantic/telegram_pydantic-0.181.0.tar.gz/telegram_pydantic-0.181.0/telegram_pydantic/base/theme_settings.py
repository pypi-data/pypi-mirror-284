from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# ThemeSettings - Layer 181
ThemeSettings = typing.Annotated[
    typing.Union[
        types.ThemeSettings
    ],
    pydantic.Field(discriminator='QUALNAME')
]
