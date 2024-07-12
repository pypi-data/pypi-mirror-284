from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPhotoEmpty(BaseModel):
    """
    types.InputPhotoEmpty
    ID: 0x1cd7bf0d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPhotoEmpty'] = pydantic.Field(
        'types.InputPhotoEmpty',
        alias='_'
    )

