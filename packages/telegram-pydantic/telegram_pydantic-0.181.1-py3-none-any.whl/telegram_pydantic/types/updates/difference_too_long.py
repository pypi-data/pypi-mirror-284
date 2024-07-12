from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DifferenceTooLong(BaseModel):
    """
    types.updates.DifferenceTooLong
    ID: 0x4afe8f6d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.updates.DifferenceTooLong'] = pydantic.Field(
        'types.updates.DifferenceTooLong',
        alias='_'
    )

    pts: int
