from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendMessageUploadDocumentAction(BaseModel):
    """
    types.SendMessageUploadDocumentAction
    ID: 0xaa0cd9e4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SendMessageUploadDocumentAction'] = pydantic.Field(
        'types.SendMessageUploadDocumentAction',
        alias='_'
    )

    progress: int
