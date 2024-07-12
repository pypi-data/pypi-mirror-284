from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# ChatInviteImporter - Layer 181
ChatInviteImporter = typing.Annotated[
    typing.Union[
        types.ChatInviteImporter
    ],
    pydantic.Field(discriminator='QUALNAME')
]
