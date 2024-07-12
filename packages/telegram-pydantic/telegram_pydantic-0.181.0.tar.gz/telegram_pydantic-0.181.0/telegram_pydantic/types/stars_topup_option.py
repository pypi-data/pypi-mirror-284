from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StarsTopupOption(BaseModel):
    """
    types.StarsTopupOption
    ID: 0xbd915c0
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StarsTopupOption'] = pydantic.Field(
        'types.StarsTopupOption',
        alias='_'
    )

    stars: int
    currency: str
    amount: int
    extended: typing.Optional[bool] = None
    store_product: typing.Optional[str] = None
