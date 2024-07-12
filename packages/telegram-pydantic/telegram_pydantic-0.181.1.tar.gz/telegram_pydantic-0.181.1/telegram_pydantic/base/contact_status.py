from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# ContactStatus - Layer 181
ContactStatus = typing.Annotated[
    typing.Union[
        types.ContactStatus
    ],
    pydantic.Field(discriminator='QUALNAME')
]
