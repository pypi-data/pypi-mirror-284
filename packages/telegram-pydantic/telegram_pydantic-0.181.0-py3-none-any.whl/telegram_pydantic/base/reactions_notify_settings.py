from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# ReactionsNotifySettings - Layer 181
ReactionsNotifySettings = typing.Annotated[
    typing.Union[
        types.ReactionsNotifySettings
    ],
    pydantic.Field(discriminator='QUALNAME')
]
