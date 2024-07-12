from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# PeerNotifySettings - Layer 181
PeerNotifySettings = typing.Annotated[
    typing.Union[
        types.PeerNotifySettings
    ],
    pydantic.Field(discriminator='QUALNAME')
]
