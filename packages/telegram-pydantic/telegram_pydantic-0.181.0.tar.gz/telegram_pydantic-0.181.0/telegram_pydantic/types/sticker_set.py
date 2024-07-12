from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StickerSet(BaseModel):
    """
    types.StickerSet
    ID: 0x2dd14edc
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StickerSet'] = pydantic.Field(
        'types.StickerSet',
        alias='_'
    )

    id: int
    access_hash: int
    title: str
    short_name: str
    count: int
    hash: int
    archived: typing.Optional[bool] = None
    official: typing.Optional[bool] = None
    masks: typing.Optional[bool] = None
    emojis: typing.Optional[bool] = None
    text_color: typing.Optional[bool] = None
    channel_emoji_status: typing.Optional[bool] = None
    creator: typing.Optional[bool] = None
    installed_date: typing.Optional[int] = None
    thumbs: typing.Optional[list["base.PhotoSize"]] = None
    thumb_dc_id: typing.Optional[int] = None
    thumb_version: typing.Optional[int] = None
    thumb_document_id: typing.Optional[int] = None
