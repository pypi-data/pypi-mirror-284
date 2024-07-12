from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdatesTooLong(BaseModel):
    """
    types.UpdatesTooLong
    ID: 0xe317af7e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdatesTooLong'] = pydantic.Field(
        'types.UpdatesTooLong',
        alias='_'
    )

