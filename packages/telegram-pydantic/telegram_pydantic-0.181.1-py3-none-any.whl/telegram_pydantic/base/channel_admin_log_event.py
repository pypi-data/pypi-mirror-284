from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# ChannelAdminLogEvent - Layer 181
ChannelAdminLogEvent = typing.Annotated[
    typing.Union[
        types.ChannelAdminLogEvent
    ],
    pydantic.Field(discriminator='QUALNAME')
]
