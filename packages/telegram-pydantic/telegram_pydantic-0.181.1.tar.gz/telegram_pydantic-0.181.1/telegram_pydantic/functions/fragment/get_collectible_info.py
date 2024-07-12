from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetCollectibleInfo(BaseModel):
    """
    functions.fragment.GetCollectibleInfo
    ID: 0xbe1e85ba
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.fragment.GetCollectibleInfo'] = pydantic.Field(
        'functions.fragment.GetCollectibleInfo',
        alias='_'
    )

    collectible: "base.InputCollectible"
