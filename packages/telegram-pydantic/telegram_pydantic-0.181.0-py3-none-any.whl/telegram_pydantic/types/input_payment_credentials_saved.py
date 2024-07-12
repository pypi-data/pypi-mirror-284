from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPaymentCredentialsSaved(BaseModel):
    """
    types.InputPaymentCredentialsSaved
    ID: 0xc10eb2cf
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPaymentCredentialsSaved'] = pydantic.Field(
        'types.InputPaymentCredentialsSaved',
        alias='_'
    )

    id: str
    tmp_password: bytes
