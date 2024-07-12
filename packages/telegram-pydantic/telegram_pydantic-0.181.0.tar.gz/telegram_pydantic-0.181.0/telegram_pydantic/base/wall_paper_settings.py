from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# WallPaperSettings - Layer 181
WallPaperSettings = typing.Annotated[
    typing.Union[
        types.WallPaperSettings
    ],
    pydantic.Field(discriminator='QUALNAME')
]
