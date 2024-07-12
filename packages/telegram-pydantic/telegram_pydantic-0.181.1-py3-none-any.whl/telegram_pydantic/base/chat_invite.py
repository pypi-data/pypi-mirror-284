from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# ChatInvite - Layer 181
ChatInvite = typing.Annotated[
    typing.Union[
        types.ChatInvite,
        types.ChatInviteAlready,
        types.ChatInvitePeek
    ],
    pydantic.Field(discriminator='QUALNAME')
]
