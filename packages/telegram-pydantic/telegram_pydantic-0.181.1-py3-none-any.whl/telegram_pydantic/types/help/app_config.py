from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AppConfig(BaseModel):
    """
    types.help.AppConfig
    ID: 0xdd18782e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.help.AppConfig'] = pydantic.Field(
        'types.help.AppConfig',
        alias='_'
    )

    hash: int
    config: "base.JSONValue"
