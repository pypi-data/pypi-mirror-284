from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ExportedMessageLink(BaseModel):
    """
    types.ExportedMessageLink
    ID: 0x5dab1af4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ExportedMessageLink'] = pydantic.Field(
        'types.ExportedMessageLink',
        alias='_'
    )

    link: str
    html: str
