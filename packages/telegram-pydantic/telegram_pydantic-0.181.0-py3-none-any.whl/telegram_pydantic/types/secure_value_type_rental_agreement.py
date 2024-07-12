from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecureValueTypeRentalAgreement(BaseModel):
    """
    types.SecureValueTypeRentalAgreement
    ID: 0x8b883488
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecureValueTypeRentalAgreement'] = pydantic.Field(
        'types.SecureValueTypeRentalAgreement',
        alias='_'
    )

