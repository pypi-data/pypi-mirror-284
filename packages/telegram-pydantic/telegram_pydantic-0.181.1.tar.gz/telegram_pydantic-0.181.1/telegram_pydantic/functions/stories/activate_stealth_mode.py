from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ActivateStealthMode(BaseModel):
    """
    functions.stories.ActivateStealthMode
    ID: 0x57bbd166
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stories.ActivateStealthMode'] = pydantic.Field(
        'functions.stories.ActivateStealthMode',
        alias='_'
    )

    past: typing.Optional[bool] = None
    future: typing.Optional[bool] = None
