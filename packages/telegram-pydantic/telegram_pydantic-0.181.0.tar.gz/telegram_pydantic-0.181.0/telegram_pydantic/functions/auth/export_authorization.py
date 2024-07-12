from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ExportAuthorization(BaseModel):
    """
    functions.auth.ExportAuthorization
    ID: 0xe5bfffcd
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.auth.ExportAuthorization'] = pydantic.Field(
        'functions.auth.ExportAuthorization',
        alias='_'
    )

    dc_id: int
