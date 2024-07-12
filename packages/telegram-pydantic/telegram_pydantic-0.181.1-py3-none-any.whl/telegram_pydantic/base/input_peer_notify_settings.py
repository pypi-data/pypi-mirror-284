from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputPeerNotifySettings - Layer 181
InputPeerNotifySettings = typing.Annotated[
    typing.Union[
        types.InputPeerNotifySettings
    ],
    pydantic.Field(discriminator='QUALNAME')
]
