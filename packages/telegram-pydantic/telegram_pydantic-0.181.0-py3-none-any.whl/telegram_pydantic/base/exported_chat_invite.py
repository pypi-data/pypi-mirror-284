from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# ExportedChatInvite - Layer 181
ExportedChatInvite = typing.Annotated[
    typing.Union[
        types.ChatInviteExported,
        types.ChatInvitePublicJoinRequests
    ],
    pydantic.Field(discriminator='QUALNAME')
]
