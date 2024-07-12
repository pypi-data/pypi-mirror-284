from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetStarsStatus(BaseModel):
    """
    functions.payments.GetStarsStatus
    ID: 0x104fcfa7
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.payments.GetStarsStatus'] = pydantic.Field(
        'functions.payments.GetStarsStatus',
        alias='_'
    )

    peer: "base.InputPeer"
