from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# help.AppConfig - Layer 181
AppConfig = typing.Annotated[
    typing.Union[
        types.help.AppConfig,
        types.help.AppConfigNotModified
    ],
    pydantic.Field(discriminator='QUALNAME')
]
