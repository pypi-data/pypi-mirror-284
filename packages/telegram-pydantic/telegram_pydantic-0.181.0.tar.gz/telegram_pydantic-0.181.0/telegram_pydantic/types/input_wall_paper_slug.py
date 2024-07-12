from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputWallPaperSlug(BaseModel):
    """
    types.InputWallPaperSlug
    ID: 0x72091c80
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputWallPaperSlug'] = pydantic.Field(
        'types.InputWallPaperSlug',
        alias='_'
    )

    slug: str
