from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SupportName(BaseModel):
    """
    types.help.SupportName
    ID: 0x8c05f1c9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.help.SupportName'] = pydantic.Field(
        'types.help.SupportName',
        alias='_'
    )

    name: str
