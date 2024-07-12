from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetSupport(BaseModel):
    """
    functions.help.GetSupport
    ID: 0x9cdf08cd
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.help.GetSupport'] = pydantic.Field(
        'functions.help.GetSupport',
        alias='_'
    )

