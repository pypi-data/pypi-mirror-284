from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetBoostsList(BaseModel):
    """
    functions.premium.GetBoostsList
    ID: 0x60f67660
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.premium.GetBoostsList'] = pydantic.Field(
        'functions.premium.GetBoostsList',
        alias='_'
    )

    peer: "base.InputPeer"
    offset: str
    limit: int
    gifts: typing.Optional[bool] = None
