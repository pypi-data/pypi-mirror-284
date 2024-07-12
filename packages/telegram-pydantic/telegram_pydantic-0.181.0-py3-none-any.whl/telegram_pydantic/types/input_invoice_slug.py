from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputInvoiceSlug(BaseModel):
    """
    types.InputInvoiceSlug
    ID: 0xc326caef
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputInvoiceSlug'] = pydantic.Field(
        'types.InputInvoiceSlug',
        alias='_'
    )

    slug: str
