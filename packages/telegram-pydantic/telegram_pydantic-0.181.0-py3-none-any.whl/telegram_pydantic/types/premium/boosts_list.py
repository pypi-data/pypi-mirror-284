from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BoostsList(BaseModel):
    """
    types.premium.BoostsList
    ID: 0x86f8613c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.premium.BoostsList'] = pydantic.Field(
        'types.premium.BoostsList',
        alias='_'
    )

    count: int
    boosts: list["base.Boost"]
    users: list["base.User"]
    next_offset: typing.Optional[str] = None
