from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CdnPublicKey(BaseModel):
    """
    types.CdnPublicKey
    ID: 0xc982eaba
    Layer: 181
    """
    QUALNAME: typing.Literal['types.CdnPublicKey'] = pydantic.Field(
        'types.CdnPublicKey',
        alias='_'
    )

    dc_id: int
    public_key: str
