from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputEncryptedFileLocation(BaseModel):
    """
    types.InputEncryptedFileLocation
    ID: 0xf5235d55
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputEncryptedFileLocation'] = pydantic.Field(
        'types.InputEncryptedFileLocation',
        alias='_'
    )

    id: int
    access_hash: int
