from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# LangPackLanguage - Layer 181
LangPackLanguage = typing.Annotated[
    typing.Union[
        types.LangPackLanguage
    ],
    pydantic.Field(discriminator='QUALNAME')
]
