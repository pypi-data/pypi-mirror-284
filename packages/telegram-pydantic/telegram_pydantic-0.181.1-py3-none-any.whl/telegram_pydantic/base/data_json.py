from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# DataJSON - Layer 181
DataJSON = typing.Annotated[
    typing.Union[
        types.DataJSON
    ],
    pydantic.Field(discriminator='QUALNAME')
]
