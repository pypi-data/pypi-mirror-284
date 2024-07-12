from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetStarsTopupOptions(BaseModel):
    """
    functions.payments.GetStarsTopupOptions
    ID: 0xc00ec7d3
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.payments.GetStarsTopupOptions'] = pydantic.Field(
        'functions.payments.GetStarsTopupOptions',
        alias='_'
    )

