from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# QuickReply - Layer 181
QuickReply = typing.Annotated[
    typing.Union[
        types.QuickReply
    ],
    pydantic.Field(discriminator='QUALNAME')
]
