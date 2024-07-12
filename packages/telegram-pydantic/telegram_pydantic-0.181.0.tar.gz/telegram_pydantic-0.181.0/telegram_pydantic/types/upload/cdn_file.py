from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CdnFile(BaseModel):
    """
    types.upload.CdnFile
    ID: 0xa99fca4f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.upload.CdnFile'] = pydantic.Field(
        'types.upload.CdnFile',
        alias='_'
    )

    bytes: bytes
