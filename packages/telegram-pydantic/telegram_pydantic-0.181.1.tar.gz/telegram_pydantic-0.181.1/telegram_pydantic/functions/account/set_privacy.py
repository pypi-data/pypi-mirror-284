from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetPrivacy(BaseModel):
    """
    functions.account.SetPrivacy
    ID: 0xc9f81ce8
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.SetPrivacy'] = pydantic.Field(
        'functions.account.SetPrivacy',
        alias='_'
    )

    key: "base.InputPrivacyKey"
    rules: list["base.InputPrivacyRule"]
