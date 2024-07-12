from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# TextWithEntities - Layer 181
TextWithEntities = typing.Annotated[
    typing.Union[
        types.TextWithEntities
    ],
    pydantic.Field(discriminator='QUALNAME')
]
