from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# ChatAdminWithInvites - Layer 181
ChatAdminWithInvites = typing.Annotated[
    typing.Union[
        types.ChatAdminWithInvites
    ],
    pydantic.Field(discriminator='QUALNAME')
]
