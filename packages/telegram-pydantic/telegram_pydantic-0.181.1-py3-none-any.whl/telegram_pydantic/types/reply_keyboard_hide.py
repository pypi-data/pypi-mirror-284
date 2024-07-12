from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReplyKeyboardHide(BaseModel):
    """
    types.ReplyKeyboardHide
    ID: 0xa03e5b85
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ReplyKeyboardHide'] = pydantic.Field(
        'types.ReplyKeyboardHide',
        alias='_'
    )

    selective: typing.Optional[bool] = None
