from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendAsPeer(BaseModel):
    """
    types.SendAsPeer
    ID: 0xb81c7034
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SendAsPeer'] = pydantic.Field(
        'types.SendAsPeer',
        alias='_'
    )

    peer: "base.Peer"
    premium_required: typing.Optional[bool] = None
