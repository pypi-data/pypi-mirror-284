from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# ChatBannedRights - Layer 181
ChatBannedRights = typing.Annotated[
    typing.Union[
        types.ChatBannedRights
    ],
    pydantic.Field(discriminator='QUALNAME')
]
