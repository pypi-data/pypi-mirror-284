from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# Chat - Layer 181
Chat = typing.Annotated[
    typing.Union[
        types.Channel,
        types.ChannelForbidden,
        types.Chat,
        types.ChatEmpty,
        types.ChatForbidden
    ],
    pydantic.Field(discriminator='QUALNAME')
]
