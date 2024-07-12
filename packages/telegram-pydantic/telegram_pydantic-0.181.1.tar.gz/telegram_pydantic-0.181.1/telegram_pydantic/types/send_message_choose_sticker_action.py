from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendMessageChooseStickerAction(BaseModel):
    """
    types.SendMessageChooseStickerAction
    ID: 0xb05ac6b1
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SendMessageChooseStickerAction'] = pydantic.Field(
        'types.SendMessageChooseStickerAction',
        alias='_'
    )

