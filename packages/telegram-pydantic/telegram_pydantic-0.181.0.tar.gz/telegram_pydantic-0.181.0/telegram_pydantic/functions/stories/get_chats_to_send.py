from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetChatsToSend(BaseModel):
    """
    functions.stories.GetChatsToSend
    ID: 0xa56a8b60
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stories.GetChatsToSend'] = pydantic.Field(
        'functions.stories.GetChatsToSend',
        alias='_'
    )

