from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.SavedGifs - Layer 181
SavedGifs = typing.Annotated[
    typing.Union[
        types.messages.SavedGifs,
        types.messages.SavedGifsNotModified
    ],
    pydantic.Field(discriminator='QUALNAME')
]
