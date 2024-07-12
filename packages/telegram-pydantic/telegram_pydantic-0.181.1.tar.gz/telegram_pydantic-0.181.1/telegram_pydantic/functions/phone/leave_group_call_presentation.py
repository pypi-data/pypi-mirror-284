from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class LeaveGroupCallPresentation(BaseModel):
    """
    functions.phone.LeaveGroupCallPresentation
    ID: 0x1c50d144
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.phone.LeaveGroupCallPresentation'] = pydantic.Field(
        'functions.phone.LeaveGroupCallPresentation',
        alias='_'
    )

    call: "base.InputGroupCall"
