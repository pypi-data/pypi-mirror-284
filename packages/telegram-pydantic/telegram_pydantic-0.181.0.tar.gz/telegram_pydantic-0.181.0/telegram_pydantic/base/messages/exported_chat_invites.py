from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.ExportedChatInvites - Layer 181
ExportedChatInvites = typing.Annotated[
    typing.Union[
        types.messages.ExportedChatInvites
    ],
    pydantic.Field(discriminator='QUALNAME')
]
