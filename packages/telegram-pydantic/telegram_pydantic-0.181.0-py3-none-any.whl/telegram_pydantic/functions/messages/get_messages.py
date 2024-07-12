from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetMessages(BaseModel):
    """
    functions.messages.GetMessages
    ID: 0x63c66506
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetMessages'] = pydantic.Field(
        'functions.messages.GetMessages',
        alias='_'
    )

    id: list["base.InputMessage"]
