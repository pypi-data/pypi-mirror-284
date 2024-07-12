from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetAppUpdate(BaseModel):
    """
    functions.help.GetAppUpdate
    ID: 0x522d5a7d
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.help.GetAppUpdate'] = pydantic.Field(
        'functions.help.GetAppUpdate',
        alias='_'
    )

    source: str
