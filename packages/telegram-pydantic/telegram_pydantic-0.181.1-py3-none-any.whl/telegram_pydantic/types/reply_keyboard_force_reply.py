from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReplyKeyboardForceReply(BaseModel):
    """
    types.ReplyKeyboardForceReply
    ID: 0x86b40b08
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ReplyKeyboardForceReply'] = pydantic.Field(
        'types.ReplyKeyboardForceReply',
        alias='_'
    )

    single_use: typing.Optional[bool] = None
    selective: typing.Optional[bool] = None
    placeholder: typing.Optional[str] = None
