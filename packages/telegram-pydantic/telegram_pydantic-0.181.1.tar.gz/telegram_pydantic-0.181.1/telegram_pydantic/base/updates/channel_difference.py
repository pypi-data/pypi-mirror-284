from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# updates.ChannelDifference - Layer 181
ChannelDifference = typing.Annotated[
    typing.Union[
        types.updates.ChannelDifference,
        types.updates.ChannelDifferenceEmpty,
        types.updates.ChannelDifferenceTooLong
    ],
    pydantic.Field(discriminator='QUALNAME')
]
