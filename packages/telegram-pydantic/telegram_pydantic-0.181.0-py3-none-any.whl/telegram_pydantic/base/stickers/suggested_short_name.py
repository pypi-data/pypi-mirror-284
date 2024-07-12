from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# stickers.SuggestedShortName - Layer 181
SuggestedShortName = typing.Annotated[
    typing.Union[
        types.stickers.SuggestedShortName
    ],
    pydantic.Field(discriminator='QUALNAME')
]
