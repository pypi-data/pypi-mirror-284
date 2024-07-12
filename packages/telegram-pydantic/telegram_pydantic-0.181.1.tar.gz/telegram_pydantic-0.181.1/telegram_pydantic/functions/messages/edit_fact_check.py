from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EditFactCheck(BaseModel):
    """
    functions.messages.EditFactCheck
    ID: 0x589ee75
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.EditFactCheck'] = pydantic.Field(
        'functions.messages.EditFactCheck',
        alias='_'
    )

    peer: "base.InputPeer"
    msg_id: int
    text: "base.TextWithEntities"
