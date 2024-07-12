from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AppWebViewResultUrl(BaseModel):
    """
    types.AppWebViewResultUrl
    ID: 0x3c1b4f0d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.AppWebViewResultUrl'] = pydantic.Field(
        'types.AppWebViewResultUrl',
        alias='_'
    )

    url: str
