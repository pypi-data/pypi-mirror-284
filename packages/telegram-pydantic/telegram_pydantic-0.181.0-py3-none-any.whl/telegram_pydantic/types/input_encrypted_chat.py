from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputEncryptedChat(BaseModel):
    """
    types.InputEncryptedChat
    ID: 0xf141b5e1
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputEncryptedChat'] = pydantic.Field(
        'types.InputEncryptedChat',
        alias='_'
    )

    chat_id: int
    access_hash: int
