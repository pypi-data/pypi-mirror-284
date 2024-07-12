from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputStickerSetID(BaseModel):
    """
    types.InputStickerSetID
    ID: 0x9de7a269
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputStickerSetID'] = pydantic.Field(
        'types.InputStickerSetID',
        alias='_'
    )

    id: int
    access_hash: int
