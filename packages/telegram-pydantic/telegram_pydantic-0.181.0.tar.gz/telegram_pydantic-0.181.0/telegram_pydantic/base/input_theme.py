from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputTheme - Layer 181
InputTheme = typing.Annotated[
    typing.Union[
        types.InputTheme,
        types.InputThemeSlug
    ],
    pydantic.Field(discriminator='QUALNAME')
]
