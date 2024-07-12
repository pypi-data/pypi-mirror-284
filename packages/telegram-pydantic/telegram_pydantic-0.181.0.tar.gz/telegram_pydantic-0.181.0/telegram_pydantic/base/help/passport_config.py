from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# help.PassportConfig - Layer 181
PassportConfig = typing.Annotated[
    typing.Union[
        types.help.PassportConfig,
        types.help.PassportConfigNotModified
    ],
    pydantic.Field(discriminator='QUALNAME')
]
