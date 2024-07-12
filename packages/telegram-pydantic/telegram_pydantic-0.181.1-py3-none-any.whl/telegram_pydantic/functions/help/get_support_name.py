from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetSupportName(BaseModel):
    """
    functions.help.GetSupportName
    ID: 0xd360e72c
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.help.GetSupportName'] = pydantic.Field(
        'functions.help.GetSupportName',
        alias='_'
    )

