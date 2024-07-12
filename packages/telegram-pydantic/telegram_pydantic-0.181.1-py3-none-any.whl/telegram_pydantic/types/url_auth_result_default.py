from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UrlAuthResultDefault(BaseModel):
    """
    types.UrlAuthResultDefault
    ID: 0xa9d6db1f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UrlAuthResultDefault'] = pydantic.Field(
        'types.UrlAuthResultDefault',
        alias='_'
    )

