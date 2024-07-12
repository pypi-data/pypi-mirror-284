from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputMessage - Layer 181
InputMessage = typing.Annotated[
    typing.Union[
        types.InputMessageCallbackQuery,
        types.InputMessageID,
        types.InputMessagePinned,
        types.InputMessageReplyTo
    ],
    pydantic.Field(discriminator='QUALNAME')
]
