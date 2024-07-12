from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# account.BusinessChatLinks - Layer 181
BusinessChatLinks = typing.Annotated[
    typing.Union[
        types.account.BusinessChatLinks
    ],
    pydantic.Field(discriminator='QUALNAME')
]
