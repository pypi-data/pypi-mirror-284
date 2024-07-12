from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateTheme(BaseModel):
    """
    types.UpdateTheme
    ID: 0x8216fba3
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateTheme'] = pydantic.Field(
        'types.UpdateTheme',
        alias='_'
    )

    theme: "base.Theme"
