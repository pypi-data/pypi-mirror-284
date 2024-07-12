from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageExtendedMedia(BaseModel):
    """
    types.MessageExtendedMedia
    ID: 0xee479c64
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageExtendedMedia'] = pydantic.Field(
        'types.MessageExtendedMedia',
        alias='_'
    )

    media: "base.MessageMedia"
