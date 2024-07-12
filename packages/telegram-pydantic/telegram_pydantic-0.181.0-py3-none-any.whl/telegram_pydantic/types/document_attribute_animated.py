from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DocumentAttributeAnimated(BaseModel):
    """
    types.DocumentAttributeAnimated
    ID: 0x11b58939
    Layer: 181
    """
    QUALNAME: typing.Literal['types.DocumentAttributeAnimated'] = pydantic.Field(
        'types.DocumentAttributeAnimated',
        alias='_'
    )

