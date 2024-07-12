from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.StickerSet - Layer 181
StickerSet = typing.Annotated[
    typing.Union[
        types.messages.StickerSet,
        types.messages.StickerSetNotModified
    ],
    pydantic.Field(discriminator='QUALNAME')
]
