from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# CdnConfig - Layer 181
CdnConfig = typing.Annotated[
    typing.Union[
        types.CdnConfig
    ],
    pydantic.Field(discriminator='QUALNAME')
]
