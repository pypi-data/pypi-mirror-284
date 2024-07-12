from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# ExportedMessageLink - Layer 181
ExportedMessageLink = typing.Annotated[
    typing.Union[
        types.ExportedMessageLink
    ],
    pydantic.Field(discriminator='QUALNAME')
]
