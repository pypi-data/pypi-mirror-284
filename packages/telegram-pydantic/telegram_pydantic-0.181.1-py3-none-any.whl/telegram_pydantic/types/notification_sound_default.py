from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class NotificationSoundDefault(BaseModel):
    """
    types.NotificationSoundDefault
    ID: 0x97e8bebe
    Layer: 181
    """
    QUALNAME: typing.Literal['types.NotificationSoundDefault'] = pydantic.Field(
        'types.NotificationSoundDefault',
        alias='_'
    )

