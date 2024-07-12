from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendMessageUploadVideoAction(BaseModel):
    """
    types.SendMessageUploadVideoAction
    ID: 0xe9763aec
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SendMessageUploadVideoAction'] = pydantic.Field(
        'types.SendMessageUploadVideoAction',
        alias='_'
    )

    progress: int
