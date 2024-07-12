from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# StickerSetCovered - Layer 181
StickerSetCovered = typing.Annotated[
    typing.Union[
        types.StickerSetCovered,
        types.StickerSetFullCovered,
        types.StickerSetMultiCovered,
        types.StickerSetNoCovered
    ],
    pydantic.Field(discriminator='QUALNAME')
]
