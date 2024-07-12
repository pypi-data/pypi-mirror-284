from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# BusinessLocation - Layer 181
BusinessLocation = typing.Annotated[
    typing.Union[
        types.BusinessLocation
    ],
    pydantic.Field(discriminator='QUALNAME')
]
