from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AvailableReaction(BaseModel):
    """
    types.AvailableReaction
    ID: 0xc077ec01
    Layer: 181
    """
    QUALNAME: typing.Literal['types.AvailableReaction'] = pydantic.Field(
        'types.AvailableReaction',
        alias='_'
    )

    reaction: str
    title: str
    static_icon: "base.Document"
    appear_animation: "base.Document"
    select_animation: "base.Document"
    activate_animation: "base.Document"
    effect_animation: "base.Document"
    inactive: typing.Optional[bool] = None
    premium: typing.Optional[bool] = None
    around_animation: typing.Optional["base.Document"] = None
    center_icon: typing.Optional["base.Document"] = None
