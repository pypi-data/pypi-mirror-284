from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputInvoiceStars(BaseModel):
    """
    types.InputInvoiceStars
    ID: 0x1da33ad8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputInvoiceStars'] = pydantic.Field(
        'types.InputInvoiceStars',
        alias='_'
    )

    option: "base.StarsTopupOption"
