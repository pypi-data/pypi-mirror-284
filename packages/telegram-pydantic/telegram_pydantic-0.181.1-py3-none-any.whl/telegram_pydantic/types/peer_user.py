from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PeerUser(BaseModel):
    """
    types.PeerUser
    ID: 0x59511722
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PeerUser'] = pydantic.Field(
        'types.PeerUser',
        alias='_'
    )

    user_id: int
