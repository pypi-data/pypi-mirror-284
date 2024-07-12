from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# AttachMenuBotIcon - Layer 181
AttachMenuBotIcon = typing.Annotated[
    typing.Union[
        types.AttachMenuBotIcon
    ],
    pydantic.Field(discriminator='QUALNAME')
]
