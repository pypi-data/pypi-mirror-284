from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# ExportedContactToken - Layer 181
ExportedContactToken = typing.Annotated[
    typing.Union[
        types.ExportedContactToken
    ],
    pydantic.Field(discriminator='QUALNAME')
]
