from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageMediaGiveaway(BaseModel):
    """
    types.MessageMediaGiveaway
    ID: 0xdaad85b0
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageMediaGiveaway'] = pydantic.Field(
        'types.MessageMediaGiveaway',
        alias='_'
    )

    channels: list[int]
    quantity: int
    months: int
    until_date: int
    only_new_subscribers: typing.Optional[bool] = None
    winners_are_visible: typing.Optional[bool] = None
    countries_iso2: typing.Optional[list[str]] = None
    prize_description: typing.Optional[str] = None
