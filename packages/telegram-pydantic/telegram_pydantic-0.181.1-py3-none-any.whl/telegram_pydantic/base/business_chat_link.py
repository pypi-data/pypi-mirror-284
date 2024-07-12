from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# BusinessChatLink - Layer 181
BusinessChatLink = typing.Annotated[
    typing.Union[
        types.BusinessChatLink
    ],
    pydantic.Field(discriminator='QUALNAME')
]
