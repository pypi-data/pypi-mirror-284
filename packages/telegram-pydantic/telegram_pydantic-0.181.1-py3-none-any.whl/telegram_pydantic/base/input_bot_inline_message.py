from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputBotInlineMessage - Layer 181
InputBotInlineMessage = typing.Annotated[
    typing.Union[
        types.InputBotInlineMessageGame,
        types.InputBotInlineMessageMediaAuto,
        types.InputBotInlineMessageMediaContact,
        types.InputBotInlineMessageMediaGeo,
        types.InputBotInlineMessageMediaInvoice,
        types.InputBotInlineMessageMediaVenue,
        types.InputBotInlineMessageMediaWebPage,
        types.InputBotInlineMessageText
    ],
    pydantic.Field(discriminator='QUALNAME')
]
