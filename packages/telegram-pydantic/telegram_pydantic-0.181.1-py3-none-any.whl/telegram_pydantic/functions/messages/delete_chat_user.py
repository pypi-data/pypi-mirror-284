from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DeleteChatUser(BaseModel):
    """
    functions.messages.DeleteChatUser
    ID: 0xa2185cab
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.DeleteChatUser'] = pydantic.Field(
        'functions.messages.DeleteChatUser',
        alias='_'
    )

    chat_id: int
    user_id: "base.InputUser"
    revoke_history: typing.Optional[bool] = None
