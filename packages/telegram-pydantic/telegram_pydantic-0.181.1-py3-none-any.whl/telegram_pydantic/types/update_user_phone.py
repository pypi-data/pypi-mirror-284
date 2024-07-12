from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateUserPhone(BaseModel):
    """
    types.UpdateUserPhone
    ID: 0x5492a13
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateUserPhone'] = pydantic.Field(
        'types.UpdateUserPhone',
        alias='_'
    )

    user_id: int
    phone: str
