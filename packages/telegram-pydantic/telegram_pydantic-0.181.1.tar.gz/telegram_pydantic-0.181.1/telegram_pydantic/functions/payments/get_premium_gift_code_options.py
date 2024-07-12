from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetPremiumGiftCodeOptions(BaseModel):
    """
    functions.payments.GetPremiumGiftCodeOptions
    ID: 0x2757ba54
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.payments.GetPremiumGiftCodeOptions'] = pydantic.Field(
        'functions.payments.GetPremiumGiftCodeOptions',
        alias='_'
    )

    boost_peer: typing.Optional["base.InputPeer"] = None
