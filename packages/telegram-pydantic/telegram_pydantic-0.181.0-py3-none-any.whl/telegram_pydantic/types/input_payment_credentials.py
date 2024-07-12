from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPaymentCredentials(BaseModel):
    """
    types.InputPaymentCredentials
    ID: 0x3417d728
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPaymentCredentials'] = pydantic.Field(
        'types.InputPaymentCredentials',
        alias='_'
    )

    data: "base.DataJSON"
    save: typing.Optional[bool] = None
