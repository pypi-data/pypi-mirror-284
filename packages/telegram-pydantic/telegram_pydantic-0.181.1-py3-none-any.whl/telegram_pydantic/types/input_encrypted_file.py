from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputEncryptedFile(BaseModel):
    """
    types.InputEncryptedFile
    ID: 0x5a17b5e5
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputEncryptedFile'] = pydantic.Field(
        'types.InputEncryptedFile',
        alias='_'
    )

    id: int
    access_hash: int
