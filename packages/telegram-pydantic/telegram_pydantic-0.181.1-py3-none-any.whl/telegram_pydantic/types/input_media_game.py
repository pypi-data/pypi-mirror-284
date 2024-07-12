from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMediaGame(BaseModel):
    """
    types.InputMediaGame
    ID: 0xd33f43f3
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMediaGame'] = pydantic.Field(
        'types.InputMediaGame',
        alias='_'
    )

    id: "base.InputGame"
