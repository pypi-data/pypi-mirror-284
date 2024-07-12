from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SentCodeTypeApp(BaseModel):
    """
    types.auth.SentCodeTypeApp
    ID: 0x3dbb5986
    Layer: 181
    """
    QUALNAME: typing.Literal['types.auth.SentCodeTypeApp'] = pydantic.Field(
        'types.auth.SentCodeTypeApp',
        alias='_'
    )

    length: int
