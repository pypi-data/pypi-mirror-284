from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# phone.ExportedGroupCallInvite - Layer 181
ExportedGroupCallInvite = typing.Annotated[
    typing.Union[
        types.phone.ExportedGroupCallInvite
    ],
    pydantic.Field(discriminator='QUALNAME')
]
