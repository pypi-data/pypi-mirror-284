from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChatBannedRights(BaseModel):
    """
    types.ChatBannedRights
    ID: 0x9f120418
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChatBannedRights'] = pydantic.Field(
        'types.ChatBannedRights',
        alias='_'
    )

    until_date: int
    view_messages: typing.Optional[bool] = None
    send_messages: typing.Optional[bool] = None
    send_media: typing.Optional[bool] = None
    send_stickers: typing.Optional[bool] = None
    send_gifs: typing.Optional[bool] = None
    send_games: typing.Optional[bool] = None
    send_inline: typing.Optional[bool] = None
    embed_links: typing.Optional[bool] = None
    send_polls: typing.Optional[bool] = None
    change_info: typing.Optional[bool] = None
    invite_users: typing.Optional[bool] = None
    pin_messages: typing.Optional[bool] = None
    manage_topics: typing.Optional[bool] = None
    send_photos: typing.Optional[bool] = None
    send_videos: typing.Optional[bool] = None
    send_roundvideos: typing.Optional[bool] = None
    send_audios: typing.Optional[bool] = None
    send_voices: typing.Optional[bool] = None
    send_docs: typing.Optional[bool] = None
    send_plain: typing.Optional[bool] = None
