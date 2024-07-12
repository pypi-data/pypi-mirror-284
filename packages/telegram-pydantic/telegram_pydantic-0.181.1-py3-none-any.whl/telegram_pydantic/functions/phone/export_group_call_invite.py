from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ExportGroupCallInvite(BaseModel):
    """
    functions.phone.ExportGroupCallInvite
    ID: 0xe6aa647f
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.phone.ExportGroupCallInvite'] = pydantic.Field(
        'functions.phone.ExportGroupCallInvite',
        alias='_'
    )

    call: "base.InputGroupCall"
    can_self_unmute: typing.Optional[bool] = None
