from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetAppConfig(BaseModel):
    """
    functions.help.GetAppConfig
    ID: 0x61e3f854
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.help.GetAppConfig'] = pydantic.Field(
        'functions.help.GetAppConfig',
        alias='_'
    )

    hash: int
