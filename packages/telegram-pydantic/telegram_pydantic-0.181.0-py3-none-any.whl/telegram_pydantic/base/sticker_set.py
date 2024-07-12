from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# StickerSet - Layer 181
StickerSet = typing.Annotated[
    typing.Union[
        types.StickerSet
    ],
    pydantic.Field(discriminator='QUALNAME')
]
