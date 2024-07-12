from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# MessageFwdHeader - Layer 181
MessageFwdHeader = typing.Annotated[
    typing.Union[
        types.MessageFwdHeader
    ],
    pydantic.Field(discriminator='QUALNAME')
]
