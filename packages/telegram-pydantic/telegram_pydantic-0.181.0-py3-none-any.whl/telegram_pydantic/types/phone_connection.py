from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PhoneConnection(BaseModel):
    """
    types.PhoneConnection
    ID: 0x9cc123c7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PhoneConnection'] = pydantic.Field(
        'types.PhoneConnection',
        alias='_'
    )

    id: int
    ip: str
    ipv6: str
    port: int
    peer_tag: bytes
    tcp: typing.Optional[bool] = None
