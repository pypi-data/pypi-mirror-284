from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# account.AutoSaveSettings - Layer 181
AutoSaveSettings = typing.Annotated[
    typing.Union[
        types.account.AutoSaveSettings
    ],
    pydantic.Field(discriminator='QUALNAME')
]
