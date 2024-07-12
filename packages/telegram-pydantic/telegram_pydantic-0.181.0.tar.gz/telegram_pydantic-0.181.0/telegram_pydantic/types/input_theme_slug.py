from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputThemeSlug(BaseModel):
    """
    types.InputThemeSlug
    ID: 0xf5890df1
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputThemeSlug'] = pydantic.Field(
        'types.InputThemeSlug',
        alias='_'
    )

    slug: str
