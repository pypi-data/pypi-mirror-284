from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BotInlineMessageMediaGeo(BaseModel):
    """
    types.BotInlineMessageMediaGeo
    ID: 0x51846fd
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BotInlineMessageMediaGeo'] = pydantic.Field(
        'types.BotInlineMessageMediaGeo',
        alias='_'
    )

    geo: "base.GeoPoint"
    heading: typing.Optional[int] = None
    period: typing.Optional[int] = None
    proximity_notification_radius: typing.Optional[int] = None
    reply_markup: typing.Optional["base.ReplyMarkup"] = None
