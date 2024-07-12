from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CodeTypeCall(BaseModel):
    """
    types.auth.CodeTypeCall
    ID: 0x741cd3e3
    Layer: 181
    """
    QUALNAME: typing.Literal['types.auth.CodeTypeCall'] = pydantic.Field(
        'types.auth.CodeTypeCall',
        alias='_'
    )

