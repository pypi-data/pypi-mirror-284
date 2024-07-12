from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# chatlists.ChatlistUpdates - Layer 181
ChatlistUpdates = typing.Annotated[
    typing.Union[
        types.chatlists.ChatlistUpdates
    ],
    pydantic.Field(discriminator='QUALNAME')
]
