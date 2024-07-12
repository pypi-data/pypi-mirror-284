from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputChannel - Layer 181
InputChannel = typing.Annotated[
    typing.Union[
        types.InputChannel,
        types.InputChannelEmpty,
        types.InputChannelFromMessage
    ],
    pydantic.Field(discriminator='QUALNAME')
]
