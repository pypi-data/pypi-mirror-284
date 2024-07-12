from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputThemeSettings - Layer 181
InputThemeSettings = typing.Annotated[
    typing.Union[
        types.InputThemeSettings
    ],
    pydantic.Field(discriminator='QUALNAME')
]
