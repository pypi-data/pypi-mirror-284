from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class NotificationSoundLocal(BaseModel):
    """
    types.NotificationSoundLocal
    ID: 0x830b9ae4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.NotificationSoundLocal'] = pydantic.Field(
        'types.NotificationSoundLocal',
        alias='_'
    )

    title: str
    data: str
