from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# RestrictionReason - Layer 181
RestrictionReason = typing.Annotated[
    typing.Union[
        types.RestrictionReason
    ],
    pydantic.Field(discriminator='QUALNAME')
]
