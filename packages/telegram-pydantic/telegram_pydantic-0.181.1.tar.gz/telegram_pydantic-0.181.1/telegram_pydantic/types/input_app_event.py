from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputAppEvent(BaseModel):
    """
    types.InputAppEvent
    ID: 0x1d1b1245
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputAppEvent'] = pydantic.Field(
        'types.InputAppEvent',
        alias='_'
    )

    time: float
    type: str
    peer: int
    data: "base.JSONValue"
