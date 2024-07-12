from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# SponsoredMessage - Layer 181
SponsoredMessage = typing.Annotated[
    typing.Union[
        types.SponsoredMessage
    ],
    pydantic.Field(discriminator='QUALNAME')
]
