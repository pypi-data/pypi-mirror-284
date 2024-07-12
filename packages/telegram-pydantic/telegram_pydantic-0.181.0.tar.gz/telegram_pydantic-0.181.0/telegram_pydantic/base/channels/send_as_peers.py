from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# channels.SendAsPeers - Layer 181
SendAsPeers = typing.Annotated[
    typing.Union[
        types.channels.SendAsPeers
    ],
    pydantic.Field(discriminator='QUALNAME')
]
