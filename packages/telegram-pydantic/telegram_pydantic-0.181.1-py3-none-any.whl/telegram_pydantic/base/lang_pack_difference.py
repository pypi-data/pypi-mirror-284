from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# LangPackDifference - Layer 181
LangPackDifference = typing.Annotated[
    typing.Union[
        types.LangPackDifference
    ],
    pydantic.Field(discriminator='QUALNAME')
]
