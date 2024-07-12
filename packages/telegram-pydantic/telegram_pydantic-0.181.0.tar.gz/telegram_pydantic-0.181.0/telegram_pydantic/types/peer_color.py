from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PeerColor(BaseModel):
    """
    types.PeerColor
    ID: 0xb54b5acf
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PeerColor'] = pydantic.Field(
        'types.PeerColor',
        alias='_'
    )

    color: typing.Optional[int] = None
    background_emoji_id: typing.Optional[int] = None
