from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecureValueErrorTranslationFile(BaseModel):
    """
    types.SecureValueErrorTranslationFile
    ID: 0xa1144770
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecureValueErrorTranslationFile'] = pydantic.Field(
        'types.SecureValueErrorTranslationFile',
        alias='_'
    )

    type: "base.SecureValueType"
    file_hash: bytes
    text: str
