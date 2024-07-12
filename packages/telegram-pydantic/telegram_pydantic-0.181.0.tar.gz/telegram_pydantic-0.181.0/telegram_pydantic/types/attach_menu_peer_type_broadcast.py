from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AttachMenuPeerTypeBroadcast(BaseModel):
    """
    types.AttachMenuPeerTypeBroadcast
    ID: 0x7bfbdefc
    Layer: 181
    """
    QUALNAME: typing.Literal['types.AttachMenuPeerTypeBroadcast'] = pydantic.Field(
        'types.AttachMenuPeerTypeBroadcast',
        alias='_'
    )

