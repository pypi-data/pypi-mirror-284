from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class NoAppUpdate(BaseModel):
    """
    types.help.NoAppUpdate
    ID: 0xc45a6536
    Layer: 181
    """
    QUALNAME: typing.Literal['types.help.NoAppUpdate'] = pydantic.Field(
        'types.help.NoAppUpdate',
        alias='_'
    )

