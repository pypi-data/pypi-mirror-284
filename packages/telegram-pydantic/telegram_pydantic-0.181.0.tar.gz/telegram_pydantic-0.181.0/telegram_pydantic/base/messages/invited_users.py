from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.InvitedUsers - Layer 181
InvitedUsers = typing.Annotated[
    typing.Union[
        types.messages.InvitedUsers
    ],
    pydantic.Field(discriminator='QUALNAME')
]
