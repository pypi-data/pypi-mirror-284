from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputKeyboardButtonUserProfile(BaseModel):
    """
    types.InputKeyboardButtonUserProfile
    ID: 0xe988037b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputKeyboardButtonUserProfile'] = pydantic.Field(
        'types.InputKeyboardButtonUserProfile',
        alias='_'
    )

    text: str
    user_id: "base.InputUser"
