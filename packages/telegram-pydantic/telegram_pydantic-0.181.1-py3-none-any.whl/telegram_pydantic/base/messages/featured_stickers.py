from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.FeaturedStickers - Layer 181
FeaturedStickers = typing.Annotated[
    typing.Union[
        types.messages.FeaturedStickers,
        types.messages.FeaturedStickersNotModified
    ],
    pydantic.Field(discriminator='QUALNAME')
]
