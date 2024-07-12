from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CodeTypeMissedCall(BaseModel):
    """
    types.auth.CodeTypeMissedCall
    ID: 0xd61ad6ee
    Layer: 181
    """
    QUALNAME: typing.Literal['types.auth.CodeTypeMissedCall'] = pydantic.Field(
        'types.auth.CodeTypeMissedCall',
        alias='_'
    )

