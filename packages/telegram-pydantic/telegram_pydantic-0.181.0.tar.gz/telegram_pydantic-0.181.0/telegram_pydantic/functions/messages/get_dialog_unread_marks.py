from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetDialogUnreadMarks(BaseModel):
    """
    functions.messages.GetDialogUnreadMarks
    ID: 0x22e24e22
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetDialogUnreadMarks'] = pydantic.Field(
        'functions.messages.GetDialogUnreadMarks',
        alias='_'
    )

