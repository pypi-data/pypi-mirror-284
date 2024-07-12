from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMessagesFilterGif(BaseModel):
    """
    types.InputMessagesFilterGif
    ID: 0xffc86587
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMessagesFilterGif'] = pydantic.Field(
        'types.InputMessagesFilterGif',
        alias='_'
    )

