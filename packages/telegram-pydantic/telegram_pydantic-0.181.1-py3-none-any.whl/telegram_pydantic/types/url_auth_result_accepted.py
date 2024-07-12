from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UrlAuthResultAccepted(BaseModel):
    """
    types.UrlAuthResultAccepted
    ID: 0x8f8c0e4e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UrlAuthResultAccepted'] = pydantic.Field(
        'types.UrlAuthResultAccepted',
        alias='_'
    )

    url: str
