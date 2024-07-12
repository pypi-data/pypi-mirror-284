from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.CheckedHistoryImportPeer - Layer 181
CheckedHistoryImportPeer = typing.Annotated[
    typing.Union[
        types.messages.CheckedHistoryImportPeer
    ],
    pydantic.Field(discriminator='QUALNAME')
]
