from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# phone.GroupCallStreamChannels - Layer 181
GroupCallStreamChannels = typing.Annotated[
    typing.Union[
        types.phone.GroupCallStreamChannels
    ],
    pydantic.Field(discriminator='QUALNAME')
]
