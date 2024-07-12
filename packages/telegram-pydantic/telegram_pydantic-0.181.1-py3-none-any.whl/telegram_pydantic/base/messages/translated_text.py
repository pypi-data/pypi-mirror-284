from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.TranslatedText - Layer 181
TranslatedText = typing.Annotated[
    typing.Union[
        types.messages.TranslateResult
    ],
    pydantic.Field(discriminator='QUALNAME')
]
