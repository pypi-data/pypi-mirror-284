from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CodeTypeSms(BaseModel):
    """
    types.auth.CodeTypeSms
    ID: 0x72a3158c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.auth.CodeTypeSms'] = pydantic.Field(
        'types.auth.CodeTypeSms',
        alias='_'
    )

