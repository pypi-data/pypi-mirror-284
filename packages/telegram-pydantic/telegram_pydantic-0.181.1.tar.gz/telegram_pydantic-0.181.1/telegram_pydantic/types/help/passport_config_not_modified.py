from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PassportConfigNotModified(BaseModel):
    """
    types.help.PassportConfigNotModified
    ID: 0xbfb9f457
    Layer: 181
    """
    QUALNAME: typing.Literal['types.help.PassportConfigNotModified'] = pydantic.Field(
        'types.help.PassportConfigNotModified',
        alias='_'
    )

