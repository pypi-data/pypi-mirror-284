from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputCheckPasswordSRP - Layer 181
InputCheckPasswordSRP = typing.Annotated[
    typing.Union[
        types.InputCheckPasswordEmpty,
        types.InputCheckPasswordSRP
    ],
    pydantic.Field(discriminator='QUALNAME')
]
