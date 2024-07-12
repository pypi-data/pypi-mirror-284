from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# WebAuthorization - Layer 181
WebAuthorization = typing.Annotated[
    typing.Union[
        types.WebAuthorization
    ],
    pydantic.Field(discriminator='QUALNAME')
]
