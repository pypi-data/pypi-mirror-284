from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.ChatInviteImporters - Layer 181
ChatInviteImporters = typing.Annotated[
    typing.Union[
        types.messages.ChatInviteImporters
    ],
    pydantic.Field(discriminator='QUALNAME')
]
