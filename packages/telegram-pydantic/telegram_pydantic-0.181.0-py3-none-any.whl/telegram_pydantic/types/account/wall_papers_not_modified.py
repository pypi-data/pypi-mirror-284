from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class WallPapersNotModified(BaseModel):
    """
    types.account.WallPapersNotModified
    ID: 0x1c199183
    Layer: 181
    """
    QUALNAME: typing.Literal['types.account.WallPapersNotModified'] = pydantic.Field(
        'types.account.WallPapersNotModified',
        alias='_'
    )

