from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AppConfigNotModified(BaseModel):
    """
    types.help.AppConfigNotModified
    ID: 0x7cde641d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.help.AppConfigNotModified'] = pydantic.Field(
        'types.help.AppConfigNotModified',
        alias='_'
    )

