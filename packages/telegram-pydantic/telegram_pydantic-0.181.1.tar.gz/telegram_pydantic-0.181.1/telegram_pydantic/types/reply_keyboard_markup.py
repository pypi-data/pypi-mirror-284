from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReplyKeyboardMarkup(BaseModel):
    """
    types.ReplyKeyboardMarkup
    ID: 0x85dd99d1
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ReplyKeyboardMarkup'] = pydantic.Field(
        'types.ReplyKeyboardMarkup',
        alias='_'
    )

    rows: list["base.KeyboardButtonRow"]
    resize: typing.Optional[bool] = None
    single_use: typing.Optional[bool] = None
    selective: typing.Optional[bool] = None
    persistent: typing.Optional[bool] = None
    placeholder: typing.Optional[str] = None
