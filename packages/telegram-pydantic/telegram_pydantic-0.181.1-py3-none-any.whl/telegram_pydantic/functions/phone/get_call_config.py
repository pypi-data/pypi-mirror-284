from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetCallConfig(BaseModel):
    """
    functions.phone.GetCallConfig
    ID: 0x55451fa9
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.phone.GetCallConfig'] = pydantic.Field(
        'functions.phone.GetCallConfig',
        alias='_'
    )

