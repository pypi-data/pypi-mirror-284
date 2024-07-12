from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputSingleMedia(BaseModel):
    """
    types.InputSingleMedia
    ID: 0x1cc6e91f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputSingleMedia'] = pydantic.Field(
        'types.InputSingleMedia',
        alias='_'
    )

    media: "base.InputMedia"
    random_id: int
    message: str
    entities: typing.Optional[list["base.MessageEntity"]] = None
