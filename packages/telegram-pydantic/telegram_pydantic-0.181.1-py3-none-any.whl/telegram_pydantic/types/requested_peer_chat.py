from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class RequestedPeerChat(BaseModel):
    """
    types.RequestedPeerChat
    ID: 0x7307544f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.RequestedPeerChat'] = pydantic.Field(
        'types.RequestedPeerChat',
        alias='_'
    )

    chat_id: int
    title: typing.Optional[str] = None
    photo: typing.Optional["base.Photo"] = None
