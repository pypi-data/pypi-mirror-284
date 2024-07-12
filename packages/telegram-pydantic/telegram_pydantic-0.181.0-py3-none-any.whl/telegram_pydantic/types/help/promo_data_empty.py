from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PromoDataEmpty(BaseModel):
    """
    types.help.PromoDataEmpty
    ID: 0x98f6ac75
    Layer: 181
    """
    QUALNAME: typing.Literal['types.help.PromoDataEmpty'] = pydantic.Field(
        'types.help.PromoDataEmpty',
        alias='_'
    )

    expires: int
