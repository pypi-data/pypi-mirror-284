from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# LangPackString - Layer 181
LangPackString = typing.Annotated[
    typing.Union[
        types.LangPackString,
        types.LangPackStringDeleted,
        types.LangPackStringPluralized
    ],
    pydantic.Field(discriminator='QUALNAME')
]
