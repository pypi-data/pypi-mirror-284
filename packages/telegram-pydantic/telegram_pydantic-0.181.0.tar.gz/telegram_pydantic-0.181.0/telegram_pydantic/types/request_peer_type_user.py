from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class RequestPeerTypeUser(BaseModel):
    """
    types.RequestPeerTypeUser
    ID: 0x5f3b8a00
    Layer: 181
    """
    QUALNAME: typing.Literal['types.RequestPeerTypeUser'] = pydantic.Field(
        'types.RequestPeerTypeUser',
        alias='_'
    )

    bot: typing.Optional[bool] = None
    premium: typing.Optional[bool] = None
