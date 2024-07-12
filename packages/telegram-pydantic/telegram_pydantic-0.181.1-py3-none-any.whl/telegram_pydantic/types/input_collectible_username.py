from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputCollectibleUsername(BaseModel):
    """
    types.InputCollectibleUsername
    ID: 0xe39460a9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputCollectibleUsername'] = pydantic.Field(
        'types.InputCollectibleUsername',
        alias='_'
    )

    username: str
