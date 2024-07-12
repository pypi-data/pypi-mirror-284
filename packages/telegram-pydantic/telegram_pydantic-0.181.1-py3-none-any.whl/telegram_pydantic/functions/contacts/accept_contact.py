from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AcceptContact(BaseModel):
    """
    functions.contacts.AcceptContact
    ID: 0xf831a20f
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.contacts.AcceptContact'] = pydantic.Field(
        'functions.contacts.AcceptContact',
        alias='_'
    )

    id: "base.InputUser"
