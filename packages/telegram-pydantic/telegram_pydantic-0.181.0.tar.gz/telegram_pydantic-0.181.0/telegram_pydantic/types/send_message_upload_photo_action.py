from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendMessageUploadPhotoAction(BaseModel):
    """
    types.SendMessageUploadPhotoAction
    ID: 0xd1d34a26
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SendMessageUploadPhotoAction'] = pydantic.Field(
        'types.SendMessageUploadPhotoAction',
        alias='_'
    )

    progress: int
