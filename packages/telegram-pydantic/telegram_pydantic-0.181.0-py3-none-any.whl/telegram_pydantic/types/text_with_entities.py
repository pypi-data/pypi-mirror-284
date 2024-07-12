from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TextWithEntities(BaseModel):
    """
    types.TextWithEntities
    ID: 0x751f3146
    Layer: 181
    """
    QUALNAME: typing.Literal['types.TextWithEntities'] = pydantic.Field(
        'types.TextWithEntities',
        alias='_'
    )

    text: str
    entities: list["base.MessageEntity"]
