from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateMessageExtendedMedia(BaseModel):
    """
    types.UpdateMessageExtendedMedia
    ID: 0x5a73a98c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateMessageExtendedMedia'] = pydantic.Field(
        'types.UpdateMessageExtendedMedia',
        alias='_'
    )

    peer: "base.Peer"
    msg_id: int
    extended_media: "base.MessageExtendedMedia"
