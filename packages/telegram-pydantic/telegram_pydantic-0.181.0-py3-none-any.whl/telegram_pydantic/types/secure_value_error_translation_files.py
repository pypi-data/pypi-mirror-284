from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecureValueErrorTranslationFiles(BaseModel):
    """
    types.SecureValueErrorTranslationFiles
    ID: 0x34636dd8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecureValueErrorTranslationFiles'] = pydantic.Field(
        'types.SecureValueErrorTranslationFiles',
        alias='_'
    )

    type: "base.SecureValueType"
    file_hash: list[bytes]
    text: str
