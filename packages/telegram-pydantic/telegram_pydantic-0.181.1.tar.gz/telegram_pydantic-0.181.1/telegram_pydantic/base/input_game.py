from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputGame - Layer 181
InputGame = typing.Annotated[
    typing.Union[
        types.InputGameID,
        types.InputGameShortName
    ],
    pydantic.Field(discriminator='QUALNAME')
]
