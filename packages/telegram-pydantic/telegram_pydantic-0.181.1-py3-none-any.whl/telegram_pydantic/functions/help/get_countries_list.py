from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetCountriesList(BaseModel):
    """
    functions.help.GetCountriesList
    ID: 0x735787a8
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.help.GetCountriesList'] = pydantic.Field(
        'functions.help.GetCountriesList',
        alias='_'
    )

    lang_code: str
    hash: int
