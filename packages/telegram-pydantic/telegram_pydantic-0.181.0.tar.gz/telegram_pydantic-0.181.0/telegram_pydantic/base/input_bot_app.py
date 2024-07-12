from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputBotApp - Layer 181
InputBotApp = typing.Annotated[
    typing.Union[
        types.InputBotAppID,
        types.InputBotAppShortName
    ],
    pydantic.Field(discriminator='QUALNAME')
]
