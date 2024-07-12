from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class WebPageNotModified(BaseModel):
    """
    types.WebPageNotModified
    ID: 0x7311ca11
    Layer: 181
    """
    QUALNAME: typing.Literal['types.WebPageNotModified'] = pydantic.Field(
        'types.WebPageNotModified',
        alias='_'
    )

    cached_page_views: typing.Optional[int] = None
