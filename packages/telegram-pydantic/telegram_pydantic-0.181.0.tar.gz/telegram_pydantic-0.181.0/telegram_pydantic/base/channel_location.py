from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# ChannelLocation - Layer 181
ChannelLocation = typing.Annotated[
    typing.Union[
        types.ChannelLocation,
        types.ChannelLocationEmpty
    ],
    pydantic.Field(discriminator='QUALNAME')
]
