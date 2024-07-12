from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# GeoPoint - Layer 181
GeoPoint = typing.Annotated[
    typing.Union[
        types.GeoPoint,
        types.GeoPointEmpty
    ],
    pydantic.Field(discriminator='QUALNAME')
]
