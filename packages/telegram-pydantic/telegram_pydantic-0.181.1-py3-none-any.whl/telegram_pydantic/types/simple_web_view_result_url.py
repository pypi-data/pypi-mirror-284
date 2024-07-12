from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SimpleWebViewResultUrl(BaseModel):
    """
    types.SimpleWebViewResultUrl
    ID: 0x882f76bb
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SimpleWebViewResultUrl'] = pydantic.Field(
        'types.SimpleWebViewResultUrl',
        alias='_'
    )

    url: str
