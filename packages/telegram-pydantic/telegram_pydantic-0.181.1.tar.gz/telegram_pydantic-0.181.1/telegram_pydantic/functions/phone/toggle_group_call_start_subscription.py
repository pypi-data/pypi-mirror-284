from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ToggleGroupCallStartSubscription(BaseModel):
    """
    functions.phone.ToggleGroupCallStartSubscription
    ID: 0x219c34e6
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.phone.ToggleGroupCallStartSubscription'] = pydantic.Field(
        'functions.phone.ToggleGroupCallStartSubscription',
        alias='_'
    )

    call: "base.InputGroupCall"
    subscribed: bool
