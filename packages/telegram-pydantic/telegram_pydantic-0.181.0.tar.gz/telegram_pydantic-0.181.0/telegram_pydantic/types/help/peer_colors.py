from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PeerColors(BaseModel):
    """
    types.help.PeerColors
    ID: 0xf8ed08
    Layer: 181
    """
    QUALNAME: typing.Literal['types.help.PeerColors'] = pydantic.Field(
        'types.help.PeerColors',
        alias='_'
    )

    hash: int
    colors: list["base.help.PeerColorOption"]
