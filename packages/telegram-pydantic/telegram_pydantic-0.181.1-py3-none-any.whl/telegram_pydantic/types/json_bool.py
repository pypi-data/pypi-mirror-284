from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class JsonBool(BaseModel):
    """
    types.JsonBool
    ID: 0xc7345e6a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.JsonBool'] = pydantic.Field(
        'types.JsonBool',
        alias='_'
    )

    value: bool
