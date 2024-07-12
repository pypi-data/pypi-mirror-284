from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputBotAppID(BaseModel):
    """
    types.InputBotAppID
    ID: 0xa920bd7a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputBotAppID'] = pydantic.Field(
        'types.InputBotAppID',
        alias='_'
    )

    id: int
    access_hash: int
