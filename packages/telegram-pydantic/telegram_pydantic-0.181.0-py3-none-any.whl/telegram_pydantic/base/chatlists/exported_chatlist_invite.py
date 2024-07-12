from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# chatlists.ExportedChatlistInvite - Layer 181
ExportedChatlistInvite = typing.Annotated[
    typing.Union[
        types.chatlists.ExportedChatlistInvite
    ],
    pydantic.Field(discriminator='QUALNAME')
]
