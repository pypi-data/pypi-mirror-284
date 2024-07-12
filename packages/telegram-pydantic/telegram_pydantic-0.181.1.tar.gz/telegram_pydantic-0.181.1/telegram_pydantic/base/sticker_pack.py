from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# StickerPack - Layer 181
StickerPack = typing.Annotated[
    typing.Union[
        types.StickerPack
    ],
    pydantic.Field(discriminator='QUALNAME')
]
