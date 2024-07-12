from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# Authorization - Layer 181
Authorization = typing.Annotated[
    typing.Union[
        types.Authorization
    ],
    pydantic.Field(discriminator='QUALNAME')
]
