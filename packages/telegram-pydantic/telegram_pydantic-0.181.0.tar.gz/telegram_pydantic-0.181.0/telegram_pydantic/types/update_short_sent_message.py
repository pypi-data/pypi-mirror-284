from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateShortSentMessage(BaseModel):
    """
    types.UpdateShortSentMessage
    ID: 0x9015e101
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateShortSentMessage'] = pydantic.Field(
        'types.UpdateShortSentMessage',
        alias='_'
    )

    id: int
    pts: int
    pts_count: int
    date: int
    out: typing.Optional[bool] = None
    media: typing.Optional["base.MessageMedia"] = None
    entities: typing.Optional[list["base.MessageEntity"]] = None
    ttl_period: typing.Optional[int] = None
