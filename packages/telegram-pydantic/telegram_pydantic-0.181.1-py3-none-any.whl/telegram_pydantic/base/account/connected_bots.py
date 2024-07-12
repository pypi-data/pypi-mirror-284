from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# account.ConnectedBots - Layer 181
ConnectedBots = typing.Annotated[
    typing.Union[
        types.account.ConnectedBots
    ],
    pydantic.Field(discriminator='QUALNAME')
]
