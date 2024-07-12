from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.MyStickers - Layer 181
MyStickers = typing.Annotated[
    typing.Union[
        types.messages.MyStickers
    ],
    pydantic.Field(discriminator='QUALNAME')
]
