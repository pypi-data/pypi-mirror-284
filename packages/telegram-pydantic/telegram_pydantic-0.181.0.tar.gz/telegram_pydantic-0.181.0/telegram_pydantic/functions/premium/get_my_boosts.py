from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetMyBoosts(BaseModel):
    """
    functions.premium.GetMyBoosts
    ID: 0xbe77b4a
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.premium.GetMyBoosts'] = pydantic.Field(
        'functions.premium.GetMyBoosts',
        alias='_'
    )

