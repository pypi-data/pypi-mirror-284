from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.HistoryImportParsed - Layer 181
HistoryImportParsed = typing.Annotated[
    typing.Union[
        types.messages.HistoryImportParsed
    ],
    pydantic.Field(discriminator='QUALNAME')
]
