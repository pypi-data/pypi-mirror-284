from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class IsEligibleToJoin(BaseModel):
    """
    functions.smsjobs.IsEligibleToJoin
    ID: 0xedc39d0
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.smsjobs.IsEligibleToJoin'] = pydantic.Field(
        'functions.smsjobs.IsEligibleToJoin',
        alias='_'
    )

