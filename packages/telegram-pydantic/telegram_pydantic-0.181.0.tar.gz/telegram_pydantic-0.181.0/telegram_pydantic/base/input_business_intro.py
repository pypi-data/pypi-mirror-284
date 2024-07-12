from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputBusinessIntro - Layer 181
InputBusinessIntro = typing.Annotated[
    typing.Union[
        types.InputBusinessIntro
    ],
    pydantic.Field(discriminator='QUALNAME')
]
