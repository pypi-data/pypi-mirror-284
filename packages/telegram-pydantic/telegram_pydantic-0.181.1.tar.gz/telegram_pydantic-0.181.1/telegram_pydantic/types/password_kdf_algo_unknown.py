from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PasswordKdfAlgoUnknown(BaseModel):
    """
    types.PasswordKdfAlgoUnknown
    ID: 0xd45ab096
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PasswordKdfAlgoUnknown'] = pydantic.Field(
        'types.PasswordKdfAlgoUnknown',
        alias='_'
    )

