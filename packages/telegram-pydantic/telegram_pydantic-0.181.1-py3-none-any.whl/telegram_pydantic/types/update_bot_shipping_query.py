from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateBotShippingQuery(BaseModel):
    """
    types.UpdateBotShippingQuery
    ID: 0xb5aefd7d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateBotShippingQuery'] = pydantic.Field(
        'types.UpdateBotShippingQuery',
        alias='_'
    )

    query_id: int
    user_id: int
    payload: bytes
    shipping_address: "base.PostAddress"
