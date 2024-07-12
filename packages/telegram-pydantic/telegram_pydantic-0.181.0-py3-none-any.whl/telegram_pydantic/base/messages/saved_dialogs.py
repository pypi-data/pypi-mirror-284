from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.SavedDialogs - Layer 181
SavedDialogs = typing.Annotated[
    typing.Union[
        types.messages.SavedDialogs,
        types.messages.SavedDialogsNotModified,
        types.messages.SavedDialogsSlice
    ],
    pydantic.Field(discriminator='QUALNAME')
]
