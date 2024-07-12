from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.ChatAdminsWithInvites - Layer 181
ChatAdminsWithInvites = typing.Annotated[
    typing.Union[
        types.messages.ChatAdminsWithInvites
    ],
    pydantic.Field(discriminator='QUALNAME')
]
