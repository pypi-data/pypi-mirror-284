from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CdnConfig(BaseModel):
    """
    types.CdnConfig
    ID: 0x5725e40a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.CdnConfig'] = pydantic.Field(
        'types.CdnConfig',
        alias='_'
    )

    public_keys: list["base.CdnPublicKey"]
