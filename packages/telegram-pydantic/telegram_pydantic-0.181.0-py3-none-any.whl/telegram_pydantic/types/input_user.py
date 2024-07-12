from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputUser(BaseModel):
    """
    types.InputUser
    ID: 0xf21158c6
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputUser'] = pydantic.Field(
        'types.InputUser',
        alias='_'
    )

    user_id: int
    access_hash: int
