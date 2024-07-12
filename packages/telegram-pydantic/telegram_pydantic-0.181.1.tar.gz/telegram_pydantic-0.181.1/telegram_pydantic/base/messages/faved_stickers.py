from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.FavedStickers - Layer 181
FavedStickers = typing.Annotated[
    typing.Union[
        types.messages.FavedStickers,
        types.messages.FavedStickersNotModified
    ],
    pydantic.Field(discriminator='QUALNAME')
]
