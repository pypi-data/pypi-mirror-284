from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# AttachMenuBotIconColor - Layer 181
AttachMenuBotIconColor = typing.Annotated[
    typing.Union[
        types.AttachMenuBotIconColor
    ],
    pydantic.Field(discriminator='QUALNAME')
]
