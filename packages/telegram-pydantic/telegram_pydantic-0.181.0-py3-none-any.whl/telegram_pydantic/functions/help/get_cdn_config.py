from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetCdnConfig(BaseModel):
    """
    functions.help.GetCdnConfig
    ID: 0x52029342
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.help.GetCdnConfig'] = pydantic.Field(
        'functions.help.GetCdnConfig',
        alias='_'
    )

