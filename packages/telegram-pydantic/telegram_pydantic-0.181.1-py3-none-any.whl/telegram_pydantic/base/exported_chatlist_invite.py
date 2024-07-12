from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# ExportedChatlistInvite - Layer 181
ExportedChatlistInvite = typing.Annotated[
    typing.Union[
        types.ExportedChatlistInvite
    ],
    pydantic.Field(discriminator='QUALNAME')
]
