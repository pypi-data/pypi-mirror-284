from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# ChatAdminRights - Layer 181
ChatAdminRights = typing.Annotated[
    typing.Union[
        types.ChatAdminRights
    ],
    pydantic.Field(discriminator='QUALNAME')
]
