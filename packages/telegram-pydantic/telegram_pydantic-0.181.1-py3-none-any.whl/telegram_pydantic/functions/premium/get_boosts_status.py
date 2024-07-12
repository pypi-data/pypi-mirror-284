from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetBoostsStatus(BaseModel):
    """
    functions.premium.GetBoostsStatus
    ID: 0x42f1f61
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.premium.GetBoostsStatus'] = pydantic.Field(
        'functions.premium.GetBoostsStatus',
        alias='_'
    )

    peer: "base.InputPeer"
