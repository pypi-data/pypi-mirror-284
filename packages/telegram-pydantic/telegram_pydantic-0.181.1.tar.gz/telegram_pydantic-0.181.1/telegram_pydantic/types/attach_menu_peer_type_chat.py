from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AttachMenuPeerTypeChat(BaseModel):
    """
    types.AttachMenuPeerTypeChat
    ID: 0x509113f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.AttachMenuPeerTypeChat'] = pydantic.Field(
        'types.AttachMenuPeerTypeChat',
        alias='_'
    )

