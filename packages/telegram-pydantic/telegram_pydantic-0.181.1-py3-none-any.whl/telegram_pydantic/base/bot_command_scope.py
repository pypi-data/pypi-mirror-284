from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# BotCommandScope - Layer 181
BotCommandScope = typing.Annotated[
    typing.Union[
        types.BotCommandScopeChatAdmins,
        types.BotCommandScopeChats,
        types.BotCommandScopeDefault,
        types.BotCommandScopePeer,
        types.BotCommandScopePeerAdmins,
        types.BotCommandScopePeerUser,
        types.BotCommandScopeUsers
    ],
    pydantic.Field(discriminator='QUALNAME')
]
