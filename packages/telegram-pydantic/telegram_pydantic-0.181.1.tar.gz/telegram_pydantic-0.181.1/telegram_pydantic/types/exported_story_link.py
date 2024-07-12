from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ExportedStoryLink(BaseModel):
    """
    types.ExportedStoryLink
    ID: 0x3fc9053b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ExportedStoryLink'] = pydantic.Field(
        'types.ExportedStoryLink',
        alias='_'
    )

    link: str
