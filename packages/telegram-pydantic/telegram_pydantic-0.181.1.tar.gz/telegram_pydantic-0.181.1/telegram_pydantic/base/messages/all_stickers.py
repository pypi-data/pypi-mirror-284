from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.AllStickers - Layer 181
AllStickers = typing.Annotated[
    typing.Union[
        types.messages.AllStickers,
        types.messages.AllStickersNotModified
    ],
    pydantic.Field(discriminator='QUALNAME')
]
