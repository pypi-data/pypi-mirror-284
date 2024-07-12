from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MyBoosts(BaseModel):
    """
    types.premium.MyBoosts
    ID: 0x9ae228e2
    Layer: 181
    """
    QUALNAME: typing.Literal['types.premium.MyBoosts'] = pydantic.Field(
        'types.premium.MyBoosts',
        alias='_'
    )

    my_boosts: list["base.MyBoost"]
    chats: list["base.Chat"]
    users: list["base.User"]
