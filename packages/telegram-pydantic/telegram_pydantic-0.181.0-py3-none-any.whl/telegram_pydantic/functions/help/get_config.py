from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetConfig(BaseModel):
    """
    functions.help.GetConfig
    ID: 0xc4f9186b
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.help.GetConfig'] = pydantic.Field(
        'functions.help.GetConfig',
        alias='_'
    )

