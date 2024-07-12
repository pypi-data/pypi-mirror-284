from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateBotStopped(BaseModel):
    """
    types.UpdateBotStopped
    ID: 0xc4870a49
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateBotStopped'] = pydantic.Field(
        'types.UpdateBotStopped',
        alias='_'
    )

    user_id: int
    date: int
    stopped: bool
    qts: int
