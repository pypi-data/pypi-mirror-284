from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class NotificationSoundNone(BaseModel):
    """
    types.NotificationSoundNone
    ID: 0x6f0c34df
    Layer: 181
    """
    QUALNAME: typing.Literal['types.NotificationSoundNone'] = pydantic.Field(
        'types.NotificationSoundNone',
        alias='_'
    )

