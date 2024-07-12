from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CodeSettings(BaseModel):
    """
    types.CodeSettings
    ID: 0xad253d78
    Layer: 181
    """
    QUALNAME: typing.Literal['types.CodeSettings'] = pydantic.Field(
        'types.CodeSettings',
        alias='_'
    )

    allow_flashcall: typing.Optional[bool] = None
    current_number: typing.Optional[bool] = None
    allow_app_hash: typing.Optional[bool] = None
    allow_missed_call: typing.Optional[bool] = None
    allow_firebase: typing.Optional[bool] = None
    unknown_number: typing.Optional[bool] = None
    logout_tokens: typing.Optional[list[bytes]] = None
    token: typing.Optional[str] = None
    app_sandbox: typing.Optional[bool] = None
