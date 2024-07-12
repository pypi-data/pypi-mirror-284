from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class KeyboardButtonUserProfile(BaseModel):
    """
    types.KeyboardButtonUserProfile
    ID: 0x308660c1
    Layer: 181
    """
    QUALNAME: typing.Literal['types.KeyboardButtonUserProfile'] = pydantic.Field(
        'types.KeyboardButtonUserProfile',
        alias='_'
    )

    text: str
    user_id: int
