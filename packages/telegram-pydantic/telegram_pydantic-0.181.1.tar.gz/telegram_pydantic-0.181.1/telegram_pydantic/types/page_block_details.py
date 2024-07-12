from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageBlockDetails(BaseModel):
    """
    types.PageBlockDetails
    ID: 0x76768bed
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageBlockDetails'] = pydantic.Field(
        'types.PageBlockDetails',
        alias='_'
    )

    blocks: list["base.PageBlock"]
    title: "base.RichText"
    open: typing.Optional[bool] = None
