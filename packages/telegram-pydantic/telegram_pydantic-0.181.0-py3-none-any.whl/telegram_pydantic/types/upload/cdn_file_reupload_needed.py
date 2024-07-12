from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CdnFileReuploadNeeded(BaseModel):
    """
    types.upload.CdnFileReuploadNeeded
    ID: 0xeea8e46e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.upload.CdnFileReuploadNeeded'] = pydantic.Field(
        'types.upload.CdnFileReuploadNeeded',
        alias='_'
    )

    request_token: bytes
