from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# account.Themes - Layer 181
Themes = typing.Annotated[
    typing.Union[
        types.account.Themes,
        types.account.ThemesNotModified
    ],
    pydantic.Field(discriminator='QUALNAME')
]
