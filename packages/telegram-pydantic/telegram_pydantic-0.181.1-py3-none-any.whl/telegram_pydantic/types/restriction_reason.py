from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class RestrictionReason(BaseModel):
    """
    types.RestrictionReason
    ID: 0xd072acb4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.RestrictionReason'] = pydantic.Field(
        'types.RestrictionReason',
        alias='_'
    )

    platform: str
    reason: str
    text: str
