from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.ArchivedStickers - Layer 181
ArchivedStickers = typing.Annotated[
    typing.Union[
        types.messages.ArchivedStickers
    ],
    pydantic.Field(discriminator='QUALNAME')
]
