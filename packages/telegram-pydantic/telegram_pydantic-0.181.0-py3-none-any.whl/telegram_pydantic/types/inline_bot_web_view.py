from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InlineBotWebView(BaseModel):
    """
    types.InlineBotWebView
    ID: 0xb57295d5
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InlineBotWebView'] = pydantic.Field(
        'types.InlineBotWebView',
        alias='_'
    )

    text: str
    url: str
