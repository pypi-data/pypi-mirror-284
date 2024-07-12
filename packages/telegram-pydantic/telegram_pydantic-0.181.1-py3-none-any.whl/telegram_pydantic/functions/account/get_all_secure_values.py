from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetAllSecureValues(BaseModel):
    """
    functions.account.GetAllSecureValues
    ID: 0xb288bc7d
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.GetAllSecureValues'] = pydantic.Field(
        'functions.account.GetAllSecureValues',
        alias='_'
    )

