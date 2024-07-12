from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# ReplyMarkup - Layer 181
ReplyMarkup = typing.Annotated[
    typing.Union[
        types.ReplyInlineMarkup,
        types.ReplyKeyboardForceReply,
        types.ReplyKeyboardHide,
        types.ReplyKeyboardMarkup
    ],
    pydantic.Field(discriminator='QUALNAME')
]
