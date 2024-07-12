from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PeerSelfLocated(BaseModel):
    """
    types.PeerSelfLocated
    ID: 0xf8ec284b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PeerSelfLocated'] = pydantic.Field(
        'types.PeerSelfLocated',
        alias='_'
    )

    expires: int
