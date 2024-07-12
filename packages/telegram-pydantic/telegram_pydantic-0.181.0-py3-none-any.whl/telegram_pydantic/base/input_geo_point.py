from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputGeoPoint - Layer 181
InputGeoPoint = typing.Annotated[
    typing.Union[
        types.InputGeoPoint,
        types.InputGeoPointEmpty
    ],
    pydantic.Field(discriminator='QUALNAME')
]
