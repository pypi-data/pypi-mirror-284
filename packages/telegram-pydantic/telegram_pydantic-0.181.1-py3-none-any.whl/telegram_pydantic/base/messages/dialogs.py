from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.Dialogs - Layer 181
Dialogs = typing.Annotated[
    typing.Union[
        types.messages.Dialogs,
        types.messages.DialogsNotModified,
        types.messages.DialogsSlice
    ],
    pydantic.Field(discriminator='QUALNAME')
]
