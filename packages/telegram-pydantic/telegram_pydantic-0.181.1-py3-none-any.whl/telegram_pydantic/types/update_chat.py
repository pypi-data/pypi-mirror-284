from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateChat(BaseModel):
    """
    types.UpdateChat
    ID: 0xf89a6a4e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateChat'] = pydantic.Field(
        'types.UpdateChat',
        alias='_'
    )

    chat_id: int
