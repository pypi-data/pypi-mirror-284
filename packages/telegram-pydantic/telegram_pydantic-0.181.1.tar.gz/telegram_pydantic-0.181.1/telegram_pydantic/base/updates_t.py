from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# Updates - Layer 181
Updates = typing.Annotated[
    typing.Union[
        types.UpdateShort,
        types.UpdateShortChatMessage,
        types.UpdateShortMessage,
        types.UpdateShortSentMessage,
        types.Updates,
        types.UpdatesCombined,
        types.UpdatesTooLong
    ],
    pydantic.Field(discriminator='QUALNAME')
]
