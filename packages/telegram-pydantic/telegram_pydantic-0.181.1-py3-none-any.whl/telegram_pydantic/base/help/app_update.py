from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# help.AppUpdate - Layer 181
AppUpdate = typing.Annotated[
    typing.Union[
        types.help.AppUpdate,
        types.help.NoAppUpdate
    ],
    pydantic.Field(discriminator='QUALNAME')
]
