from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ThemesNotModified(BaseModel):
    """
    types.account.ThemesNotModified
    ID: 0xf41eb622
    Layer: 181
    """
    QUALNAME: typing.Literal['types.account.ThemesNotModified'] = pydantic.Field(
        'types.account.ThemesNotModified',
        alias='_'
    )

