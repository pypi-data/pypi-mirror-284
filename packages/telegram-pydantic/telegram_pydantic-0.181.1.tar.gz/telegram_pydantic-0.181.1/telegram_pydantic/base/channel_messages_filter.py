from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# ChannelMessagesFilter - Layer 181
ChannelMessagesFilter = typing.Annotated[
    typing.Union[
        types.ChannelMessagesFilter,
        types.ChannelMessagesFilterEmpty
    ],
    pydantic.Field(discriminator='QUALNAME')
]
