from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UploadImportedMedia(BaseModel):
    """
    functions.messages.UploadImportedMedia
    ID: 0x2a862092
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.UploadImportedMedia'] = pydantic.Field(
        'functions.messages.UploadImportedMedia',
        alias='_'
    )

    peer: "base.InputPeer"
    import_id: int
    file_name: str
    media: "base.InputMedia"
