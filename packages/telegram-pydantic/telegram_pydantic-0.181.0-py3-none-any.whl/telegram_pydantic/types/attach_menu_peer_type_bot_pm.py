from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AttachMenuPeerTypeBotPM(BaseModel):
    """
    types.AttachMenuPeerTypeBotPM
    ID: 0xc32bfa1a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.AttachMenuPeerTypeBotPM'] = pydantic.Field(
        'types.AttachMenuPeerTypeBotPM',
        alias='_'
    )

