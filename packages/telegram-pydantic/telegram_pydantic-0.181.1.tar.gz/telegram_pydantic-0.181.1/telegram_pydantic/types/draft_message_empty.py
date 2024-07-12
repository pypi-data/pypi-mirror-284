from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DraftMessageEmpty(BaseModel):
    """
    types.DraftMessageEmpty
    ID: 0x1b0c841a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.DraftMessageEmpty'] = pydantic.Field(
        'types.DraftMessageEmpty',
        alias='_'
    )

    date: typing.Optional[int] = None
