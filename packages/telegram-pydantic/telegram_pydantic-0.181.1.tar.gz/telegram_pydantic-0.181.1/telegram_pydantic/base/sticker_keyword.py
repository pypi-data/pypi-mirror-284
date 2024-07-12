from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# StickerKeyword - Layer 181
StickerKeyword = typing.Annotated[
    typing.Union[
        types.StickerKeyword
    ],
    pydantic.Field(discriminator='QUALNAME')
]
