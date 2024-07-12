from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# AttachMenuBots - Layer 181
AttachMenuBots = typing.Annotated[
    typing.Union[
        types.AttachMenuBots,
        types.AttachMenuBotsNotModified
    ],
    pydantic.Field(discriminator='QUALNAME')
]
