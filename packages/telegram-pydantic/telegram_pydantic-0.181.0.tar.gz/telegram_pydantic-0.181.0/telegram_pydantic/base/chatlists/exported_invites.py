from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# chatlists.ExportedInvites - Layer 181
ExportedInvites = typing.Annotated[
    typing.Union[
        types.chatlists.ExportedInvites
    ],
    pydantic.Field(discriminator='QUALNAME')
]
