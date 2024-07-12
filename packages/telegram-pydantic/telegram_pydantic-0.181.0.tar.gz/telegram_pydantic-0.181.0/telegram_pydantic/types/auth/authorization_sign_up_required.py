from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AuthorizationSignUpRequired(BaseModel):
    """
    types.auth.AuthorizationSignUpRequired
    ID: 0x44747e9a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.auth.AuthorizationSignUpRequired'] = pydantic.Field(
        'types.auth.AuthorizationSignUpRequired',
        alias='_'
    )

    terms_of_service: typing.Optional["base.help.TermsOfService"] = None
