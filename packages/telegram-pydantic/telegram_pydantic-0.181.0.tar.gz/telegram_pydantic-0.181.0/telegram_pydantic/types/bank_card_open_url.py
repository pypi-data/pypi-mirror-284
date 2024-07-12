from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BankCardOpenUrl(BaseModel):
    """
    types.BankCardOpenUrl
    ID: 0xf568028a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BankCardOpenUrl'] = pydantic.Field(
        'types.BankCardOpenUrl',
        alias='_'
    )

    url: str
    name: str
