from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateBusinessIntro(BaseModel):
    """
    functions.account.UpdateBusinessIntro
    ID: 0xa614d034
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.UpdateBusinessIntro'] = pydantic.Field(
        'functions.account.UpdateBusinessIntro',
        alias='_'
    )

    intro: typing.Optional["base.InputBusinessIntro"] = None
