from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.RecentStickers - Layer 181
RecentStickers = typing.Annotated[
    typing.Union[
        types.messages.RecentStickers,
        types.messages.RecentStickersNotModified
    ],
    pydantic.Field(discriminator='QUALNAME')
]
