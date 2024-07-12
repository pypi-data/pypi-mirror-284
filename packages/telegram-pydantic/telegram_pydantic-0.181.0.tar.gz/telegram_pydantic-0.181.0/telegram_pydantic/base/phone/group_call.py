from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# phone.GroupCall - Layer 181
GroupCall = typing.Annotated[
    typing.Union[
        types.phone.GroupCall
    ],
    pydantic.Field(discriminator='QUALNAME')
]
