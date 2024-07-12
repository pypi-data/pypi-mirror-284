from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# ChannelAdminLogEventsFilter - Layer 181
ChannelAdminLogEventsFilter = typing.Annotated[
    typing.Union[
        types.ChannelAdminLogEventsFilter
    ],
    pydantic.Field(discriminator='QUALNAME')
]
