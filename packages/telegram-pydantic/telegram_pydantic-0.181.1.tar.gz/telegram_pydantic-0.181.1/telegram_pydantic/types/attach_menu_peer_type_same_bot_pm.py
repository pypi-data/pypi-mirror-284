from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AttachMenuPeerTypeSameBotPM(BaseModel):
    """
    types.AttachMenuPeerTypeSameBotPM
    ID: 0x7d6be90e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.AttachMenuPeerTypeSameBotPM'] = pydantic.Field(
        'types.AttachMenuPeerTypeSameBotPM',
        alias='_'
    )

