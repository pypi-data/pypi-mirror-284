from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PassportConfig(BaseModel):
    """
    types.help.PassportConfig
    ID: 0xa098d6af
    Layer: 181
    """
    QUALNAME: typing.Literal['types.help.PassportConfig'] = pydantic.Field(
        'types.help.PassportConfig',
        alias='_'
    )

    hash: int
    countries_langs: "base.DataJSON"
