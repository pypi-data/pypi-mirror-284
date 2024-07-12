from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetMessagePublicForwards(BaseModel):
    """
    functions.stats.GetMessagePublicForwards
    ID: 0x5f150144
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stats.GetMessagePublicForwards'] = pydantic.Field(
        'functions.stats.GetMessagePublicForwards',
        alias='_'
    )

    channel: "base.InputChannel"
    msg_id: int
    offset: str
    limit: int
