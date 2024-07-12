from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ToggleGroupCallRecord(BaseModel):
    """
    functions.phone.ToggleGroupCallRecord
    ID: 0xf128c708
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.phone.ToggleGroupCallRecord'] = pydantic.Field(
        'functions.phone.ToggleGroupCallRecord',
        alias='_'
    )

    call: "base.InputGroupCall"
    start: typing.Optional[bool] = None
    video: typing.Optional[bool] = None
    title: typing.Optional[str] = None
    video_portrait: typing.Optional[bool] = None
