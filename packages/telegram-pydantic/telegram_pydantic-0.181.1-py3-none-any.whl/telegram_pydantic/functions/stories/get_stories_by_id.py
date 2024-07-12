from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetStoriesByID(BaseModel):
    """
    functions.stories.GetStoriesByID
    ID: 0x5774ca74
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stories.GetStoriesByID'] = pydantic.Field(
        'functions.stories.GetStoriesByID',
        alias='_'
    )

    peer: "base.InputPeer"
    id: list[int]
