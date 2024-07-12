from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateConfig(BaseModel):
    """
    types.UpdateConfig
    ID: 0xa229dd06
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateConfig'] = pydantic.Field(
        'types.UpdateConfig',
        alias='_'
    )

