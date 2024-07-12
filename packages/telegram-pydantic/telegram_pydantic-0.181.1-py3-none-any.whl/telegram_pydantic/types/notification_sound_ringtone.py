from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class NotificationSoundRingtone(BaseModel):
    """
    types.NotificationSoundRingtone
    ID: 0xff6c8049
    Layer: 181
    """
    QUALNAME: typing.Literal['types.NotificationSoundRingtone'] = pydantic.Field(
        'types.NotificationSoundRingtone',
        alias='_'
    )

    id: int
