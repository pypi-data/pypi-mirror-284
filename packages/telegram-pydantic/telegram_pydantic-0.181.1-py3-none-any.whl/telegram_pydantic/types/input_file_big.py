from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputFileBig(BaseModel):
    """
    types.InputFileBig
    ID: 0xfa4f0bb5
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputFileBig'] = pydantic.Field(
        'types.InputFileBig',
        alias='_'
    )

    id: int
    parts: int
    name: str
