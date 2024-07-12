from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EditStory(BaseModel):
    """
    functions.stories.EditStory
    ID: 0xb583ba46
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stories.EditStory'] = pydantic.Field(
        'functions.stories.EditStory',
        alias='_'
    )

    peer: "base.InputPeer"
    id: int
    media: typing.Optional["base.InputMedia"] = None
    media_areas: typing.Optional[list["base.MediaArea"]] = None
    caption: typing.Optional[str] = None
    entities: typing.Optional[list["base.MessageEntity"]] = None
    privacy_rules: typing.Optional[list["base.InputPrivacyRule"]] = None
