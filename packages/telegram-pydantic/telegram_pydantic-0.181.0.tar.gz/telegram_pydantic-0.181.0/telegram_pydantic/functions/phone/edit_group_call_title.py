from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EditGroupCallTitle(BaseModel):
    """
    functions.phone.EditGroupCallTitle
    ID: 0x1ca6ac0a
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.phone.EditGroupCallTitle'] = pydantic.Field(
        'functions.phone.EditGroupCallTitle',
        alias='_'
    )

    call: "base.InputGroupCall"
    title: str
