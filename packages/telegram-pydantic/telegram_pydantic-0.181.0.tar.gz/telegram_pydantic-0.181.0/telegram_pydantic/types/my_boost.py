from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MyBoost(BaseModel):
    """
    types.MyBoost
    ID: 0xc448415c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MyBoost'] = pydantic.Field(
        'types.MyBoost',
        alias='_'
    )

    slot: int
    date: int
    expires: int
    peer: typing.Optional["base.Peer"] = None
    cooldown_until_date: typing.Optional[int] = None
