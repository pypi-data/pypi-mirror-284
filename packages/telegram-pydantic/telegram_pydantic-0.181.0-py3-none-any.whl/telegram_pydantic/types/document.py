from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Document(BaseModel):
    """
    types.Document
    ID: 0x8fd4c4d8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.Document'] = pydantic.Field(
        'types.Document',
        alias='_'
    )

    id: int
    access_hash: int
    file_reference: bytes
    date: int
    mime_type: str
    size: int
    dc_id: int
    attributes: list["base.DocumentAttribute"]
    thumbs: typing.Optional[list["base.PhotoSize"]] = None
    video_thumbs: typing.Optional[list["base.VideoSize"]] = None
