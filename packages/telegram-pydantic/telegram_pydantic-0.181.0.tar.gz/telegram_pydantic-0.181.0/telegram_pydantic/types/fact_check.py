from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class FactCheck(BaseModel):
    """
    types.FactCheck
    ID: 0xb89bfccf
    Layer: 181
    """
    QUALNAME: typing.Literal['types.FactCheck'] = pydantic.Field(
        'types.FactCheck',
        alias='_'
    )

    hash: int
    need_check: typing.Optional[bool] = None
    country: typing.Optional[str] = None
    text: typing.Optional["base.TextWithEntities"] = None
