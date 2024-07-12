from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# chatlists.ChatlistInvite - Layer 181
ChatlistInvite = typing.Annotated[
    typing.Union[
        types.chatlists.ChatlistInvite,
        types.chatlists.ChatlistInviteAlready
    ],
    pydantic.Field(discriminator='QUALNAME')
]
