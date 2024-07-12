from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionChangePhoto(BaseModel):
    """
    types.ChannelAdminLogEventActionChangePhoto
    ID: 0x434bd2af
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionChangePhoto'] = pydantic.Field(
        'types.ChannelAdminLogEventActionChangePhoto',
        alias='_'
    )

    prev_photo: "base.Photo"
    new_photo: "base.Photo"
