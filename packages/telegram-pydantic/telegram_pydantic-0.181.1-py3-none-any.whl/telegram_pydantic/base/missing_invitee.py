from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# MissingInvitee - Layer 181
MissingInvitee = typing.Annotated[
    typing.Union[
        types.MissingInvitee
    ],
    pydantic.Field(discriminator='QUALNAME')
]
