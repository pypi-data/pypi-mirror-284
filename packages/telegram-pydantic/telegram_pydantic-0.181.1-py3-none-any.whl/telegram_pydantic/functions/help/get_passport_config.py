from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetPassportConfig(BaseModel):
    """
    functions.help.GetPassportConfig
    ID: 0xc661ad08
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.help.GetPassportConfig'] = pydantic.Field(
        'functions.help.GetPassportConfig',
        alias='_'
    )

    hash: int
