from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputFile(BaseModel):
    """
    types.InputFile
    ID: 0xf52ff27f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputFile'] = pydantic.Field(
        'types.InputFile',
        alias='_'
    )

    id: int
    parts: int
    name: str
    md5_checksum: str
