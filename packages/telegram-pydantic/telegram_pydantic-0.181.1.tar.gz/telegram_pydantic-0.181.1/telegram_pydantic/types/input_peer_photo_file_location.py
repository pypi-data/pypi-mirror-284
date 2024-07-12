from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPeerPhotoFileLocation(BaseModel):
    """
    types.InputPeerPhotoFileLocation
    ID: 0x37257e99
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPeerPhotoFileLocation'] = pydantic.Field(
        'types.InputPeerPhotoFileLocation',
        alias='_'
    )

    peer: "base.InputPeer"
    photo_id: int
    big: typing.Optional[bool] = None
