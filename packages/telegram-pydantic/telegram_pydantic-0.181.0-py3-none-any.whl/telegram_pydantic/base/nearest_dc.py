from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# NearestDc - Layer 181
NearestDc = typing.Annotated[
    typing.Union[
        types.NearestDc
    ],
    pydantic.Field(discriminator='QUALNAME')
]
