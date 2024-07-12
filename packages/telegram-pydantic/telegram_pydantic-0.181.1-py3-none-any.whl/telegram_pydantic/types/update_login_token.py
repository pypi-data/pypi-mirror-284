from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateLoginToken(BaseModel):
    """
    types.UpdateLoginToken
    ID: 0x564fe691
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateLoginToken'] = pydantic.Field(
        'types.UpdateLoginToken',
        alias='_'
    )

