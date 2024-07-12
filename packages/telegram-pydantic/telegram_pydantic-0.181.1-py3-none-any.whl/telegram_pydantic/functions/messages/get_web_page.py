from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetWebPage(BaseModel):
    """
    functions.messages.GetWebPage
    ID: 0x8d9692a3
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetWebPage'] = pydantic.Field(
        'functions.messages.GetWebPage',
        alias='_'
    )

    url: str
    hash: int
