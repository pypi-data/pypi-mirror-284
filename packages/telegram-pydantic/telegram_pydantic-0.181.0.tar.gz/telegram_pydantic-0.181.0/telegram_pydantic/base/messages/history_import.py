from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.HistoryImport - Layer 181
HistoryImport = typing.Annotated[
    typing.Union[
        types.messages.HistoryImport
    ],
    pydantic.Field(discriminator='QUALNAME')
]
