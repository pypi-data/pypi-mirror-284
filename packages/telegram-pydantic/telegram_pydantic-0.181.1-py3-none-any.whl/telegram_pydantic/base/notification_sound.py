from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# NotificationSound - Layer 181
NotificationSound = typing.Annotated[
    typing.Union[
        types.NotificationSoundDefault,
        types.NotificationSoundLocal,
        types.NotificationSoundNone,
        types.NotificationSoundRingtone
    ],
    pydantic.Field(discriminator='QUALNAME')
]
