from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AuthorizationForm(BaseModel):
    """
    types.account.AuthorizationForm
    ID: 0xad2e1cd8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.account.AuthorizationForm'] = pydantic.Field(
        'types.account.AuthorizationForm',
        alias='_'
    )

    required_types: list["base.SecureRequiredType"]
    values: list["base.SecureValue"]
    errors: list["base.SecureValueError"]
    users: list["base.User"]
    privacy_policy_url: typing.Optional[str] = None
