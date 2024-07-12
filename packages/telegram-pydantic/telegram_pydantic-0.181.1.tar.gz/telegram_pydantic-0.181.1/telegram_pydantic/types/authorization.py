from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Authorization(BaseModel):
    """
    types.Authorization
    ID: 0xad01d61d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.Authorization'] = pydantic.Field(
        'types.Authorization',
        alias='_'
    )

    hash: int
    device_model: str
    platform: str
    system_version: str
    api_id: int
    app_name: str
    app_version: str
    date_created: int
    date_active: int
    ip: str
    country: str
    region: str
    current: typing.Optional[bool] = None
    official_app: typing.Optional[bool] = None
    password_pending: typing.Optional[bool] = None
    encrypted_requests_disabled: typing.Optional[bool] = None
    call_requests_disabled: typing.Optional[bool] = None
    unconfirmed: typing.Optional[bool] = None
