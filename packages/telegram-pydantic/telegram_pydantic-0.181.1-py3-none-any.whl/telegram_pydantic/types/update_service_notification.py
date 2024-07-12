from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateServiceNotification(BaseModel):
    """
    types.UpdateServiceNotification
    ID: 0xebe46819
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateServiceNotification'] = pydantic.Field(
        'types.UpdateServiceNotification',
        alias='_'
    )

    type: str
    message: str
    media: "base.MessageMedia"
    entities: list["base.MessageEntity"]
    popup: typing.Optional[bool] = None
    invert_media: typing.Optional[bool] = None
    inbox_date: typing.Optional[int] = None
