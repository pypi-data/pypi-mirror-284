from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# GroupCallStreamChannel - Layer 181
GroupCallStreamChannel = typing.Annotated[
    typing.Union[
        types.GroupCallStreamChannel
    ],
    pydantic.Field(discriminator='QUALNAME')
]
