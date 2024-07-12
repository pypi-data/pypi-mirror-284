from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.FoundStickerSets - Layer 181
FoundStickerSets = typing.Annotated[
    typing.Union[
        types.messages.FoundStickerSets,
        types.messages.FoundStickerSetsNotModified
    ],
    pydantic.Field(discriminator='QUALNAME')
]
