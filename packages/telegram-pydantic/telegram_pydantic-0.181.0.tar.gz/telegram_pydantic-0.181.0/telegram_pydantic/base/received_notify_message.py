from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# ReceivedNotifyMessage - Layer 181
ReceivedNotifyMessage = typing.Annotated[
    typing.Union[
        types.ReceivedNotifyMessage
    ],
    pydantic.Field(discriminator='QUALNAME')
]
