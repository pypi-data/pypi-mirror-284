from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SponsoredMessage(BaseModel):
    """
    types.SponsoredMessage
    ID: 0xbdedf566
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SponsoredMessage'] = pydantic.Field(
        'types.SponsoredMessage',
        alias='_'
    )

    random_id: bytes
    url: str
    title: str
    message: str
    button_text: str
    recommended: typing.Optional[bool] = None
    can_report: typing.Optional[bool] = None
    entities: typing.Optional[list["base.MessageEntity"]] = None
    photo: typing.Optional["base.Photo"] = None
    color: typing.Optional["base.PeerColor"] = None
    sponsor_info: typing.Optional[str] = None
    additional_info: typing.Optional[str] = None
