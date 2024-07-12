from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StarsTransactionPeerAppStore(BaseModel):
    """
    types.StarsTransactionPeerAppStore
    ID: 0xb457b375
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StarsTransactionPeerAppStore'] = pydantic.Field(
        'types.StarsTransactionPeerAppStore',
        alias='_'
    )

