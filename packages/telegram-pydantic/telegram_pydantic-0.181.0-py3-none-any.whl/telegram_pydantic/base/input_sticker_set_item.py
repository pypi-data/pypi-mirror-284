from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputStickerSetItem - Layer 181
InputStickerSetItem = typing.Annotated[
    typing.Union[
        types.InputStickerSetItem
    ],
    pydantic.Field(discriminator='QUALNAME')
]
