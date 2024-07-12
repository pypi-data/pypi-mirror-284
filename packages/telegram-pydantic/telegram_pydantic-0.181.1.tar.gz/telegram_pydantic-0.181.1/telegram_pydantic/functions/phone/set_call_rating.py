from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetCallRating(BaseModel):
    """
    functions.phone.SetCallRating
    ID: 0x59ead627
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.phone.SetCallRating'] = pydantic.Field(
        'functions.phone.SetCallRating',
        alias='_'
    )

    peer: "base.InputPhoneCall"
    rating: int
    comment: str
    user_initiative: typing.Optional[bool] = None
