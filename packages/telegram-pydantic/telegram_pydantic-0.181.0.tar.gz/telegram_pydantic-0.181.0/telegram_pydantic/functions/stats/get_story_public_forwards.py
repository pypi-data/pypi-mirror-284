from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetStoryPublicForwards(BaseModel):
    """
    functions.stats.GetStoryPublicForwards
    ID: 0xa6437ef6
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stats.GetStoryPublicForwards'] = pydantic.Field(
        'functions.stats.GetStoryPublicForwards',
        alias='_'
    )

    peer: "base.InputPeer"
    id: int
    offset: str
    limit: int
