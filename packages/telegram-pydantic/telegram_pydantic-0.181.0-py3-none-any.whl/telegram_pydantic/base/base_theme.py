from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# BaseTheme - Layer 181
BaseTheme = typing.Annotated[
    typing.Union[
        types.BaseThemeArctic,
        types.BaseThemeClassic,
        types.BaseThemeDay,
        types.BaseThemeNight,
        types.BaseThemeTinted
    ],
    pydantic.Field(discriminator='QUALNAME')
]
