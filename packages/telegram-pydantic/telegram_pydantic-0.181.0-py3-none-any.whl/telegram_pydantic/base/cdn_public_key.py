from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# CdnPublicKey - Layer 181
CdnPublicKey = typing.Annotated[
    typing.Union[
        types.CdnPublicKey
    ],
    pydantic.Field(discriminator='QUALNAME')
]
