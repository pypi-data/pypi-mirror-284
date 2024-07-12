from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DialogFilterDefault(BaseModel):
    """
    types.DialogFilterDefault
    ID: 0x363293ae
    Layer: 181
    """
    QUALNAME: typing.Literal['types.DialogFilterDefault'] = pydantic.Field(
        'types.DialogFilterDefault',
        alias='_'
    )

