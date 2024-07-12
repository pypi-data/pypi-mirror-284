from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StarsTransaction(BaseModel):
    """
    types.StarsTransaction
    ID: 0xcc7079b2
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StarsTransaction'] = pydantic.Field(
        'types.StarsTransaction',
        alias='_'
    )

    id: str
    stars: int
    date: int
    peer: "base.StarsTransactionPeer"
    refund: typing.Optional[bool] = None
    title: typing.Optional[str] = None
    description: typing.Optional[str] = None
    photo: typing.Optional["base.WebDocument"] = None
