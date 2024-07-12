from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputStickeredMediaDocument(BaseModel):
    """
    types.InputStickeredMediaDocument
    ID: 0x438865b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputStickeredMediaDocument'] = pydantic.Field(
        'types.InputStickeredMediaDocument',
        alias='_'
    )

    id: "base.InputDocument"
