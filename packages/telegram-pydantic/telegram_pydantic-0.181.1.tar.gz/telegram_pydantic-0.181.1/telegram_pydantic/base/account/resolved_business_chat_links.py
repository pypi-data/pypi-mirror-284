from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# account.ResolvedBusinessChatLinks - Layer 181
ResolvedBusinessChatLinks = typing.Annotated[
    typing.Union[
        types.account.ResolvedBusinessChatLinks
    ],
    pydantic.Field(discriminator='QUALNAME')
]
