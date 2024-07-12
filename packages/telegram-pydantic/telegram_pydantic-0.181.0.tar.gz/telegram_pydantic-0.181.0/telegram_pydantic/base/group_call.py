from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# GroupCall - Layer 181
GroupCall = typing.Annotated[
    typing.Union[
        types.GroupCall,
        types.GroupCallDiscarded
    ],
    pydantic.Field(discriminator='QUALNAME')
]
