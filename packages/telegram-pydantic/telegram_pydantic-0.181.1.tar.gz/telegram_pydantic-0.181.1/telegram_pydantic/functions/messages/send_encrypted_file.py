from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendEncryptedFile(BaseModel):
    """
    functions.messages.SendEncryptedFile
    ID: 0x5559481d
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.SendEncryptedFile'] = pydantic.Field(
        'functions.messages.SendEncryptedFile',
        alias='_'
    )

    peer: "base.InputEncryptedChat"
    random_id: int
    data: bytes
    file: "base.InputEncryptedFile"
    silent: typing.Optional[bool] = None
