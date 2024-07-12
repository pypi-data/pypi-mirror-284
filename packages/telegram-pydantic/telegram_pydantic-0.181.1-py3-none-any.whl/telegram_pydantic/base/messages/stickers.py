from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.Stickers - Layer 181
Stickers = typing.Annotated[
    typing.Union[
        types.messages.Stickers,
        types.messages.StickersNotModified
    ],
    pydantic.Field(discriminator='QUALNAME')
]
