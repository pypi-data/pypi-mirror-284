from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BusinessIntro(BaseModel):
    """
    types.BusinessIntro
    ID: 0x5a0a066d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BusinessIntro'] = pydantic.Field(
        'types.BusinessIntro',
        alias='_'
    )

    title: str
    description: str
    sticker: typing.Optional["base.Document"] = None
