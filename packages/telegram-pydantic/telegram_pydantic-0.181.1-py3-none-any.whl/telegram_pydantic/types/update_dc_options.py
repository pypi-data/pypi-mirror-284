from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateDcOptions(BaseModel):
    """
    types.UpdateDcOptions
    ID: 0x8e5e9873
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateDcOptions'] = pydantic.Field(
        'types.UpdateDcOptions',
        alias='_'
    )

    dc_options: list["base.DcOption"]
