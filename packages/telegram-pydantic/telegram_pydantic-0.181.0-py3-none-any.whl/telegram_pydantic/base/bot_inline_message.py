from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# BotInlineMessage - Layer 181
BotInlineMessage = typing.Annotated[
    typing.Union[
        types.BotInlineMessageMediaAuto,
        types.BotInlineMessageMediaContact,
        types.BotInlineMessageMediaGeo,
        types.BotInlineMessageMediaInvoice,
        types.BotInlineMessageMediaVenue,
        types.BotInlineMessageMediaWebPage,
        types.BotInlineMessageText
    ],
    pydantic.Field(discriminator='QUALNAME')
]
