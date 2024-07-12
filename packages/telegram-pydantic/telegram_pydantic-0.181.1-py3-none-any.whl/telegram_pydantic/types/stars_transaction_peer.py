from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StarsTransactionPeer(BaseModel):
    """
    types.StarsTransactionPeer
    ID: 0xd80da15d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StarsTransactionPeer'] = pydantic.Field(
        'types.StarsTransactionPeer',
        alias='_'
    )

    peer: "base.Peer"
