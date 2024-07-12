from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.ExportedChatInvite - Layer 181
ExportedChatInvite = typing.Annotated[
    typing.Union[
        types.messages.ExportedChatInvite,
        types.messages.ExportedChatInviteReplaced
    ],
    pydantic.Field(discriminator='QUALNAME')
]
