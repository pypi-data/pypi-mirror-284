from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPeerChat(BaseModel):
    """
    types.InputPeerChat
    ID: 0x35a95cb9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPeerChat'] = pydantic.Field(
        'types.InputPeerChat',
        alias='_'
    )

    chat_id: int
