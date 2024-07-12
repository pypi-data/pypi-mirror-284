from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReceivedNotifyMessage(BaseModel):
    """
    types.ReceivedNotifyMessage
    ID: 0xa384b779
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ReceivedNotifyMessage'] = pydantic.Field(
        'types.ReceivedNotifyMessage',
        alias='_'
    )

    id: int
    flags: int
