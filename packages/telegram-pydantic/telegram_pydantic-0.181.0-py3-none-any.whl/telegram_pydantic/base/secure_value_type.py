from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# SecureValueType - Layer 181
SecureValueType = typing.Annotated[
    typing.Union[
        types.SecureValueTypeAddress,
        types.SecureValueTypeBankStatement,
        types.SecureValueTypeDriverLicense,
        types.SecureValueTypeEmail,
        types.SecureValueTypeIdentityCard,
        types.SecureValueTypeInternalPassport,
        types.SecureValueTypePassport,
        types.SecureValueTypePassportRegistration,
        types.SecureValueTypePersonalDetails,
        types.SecureValueTypePhone,
        types.SecureValueTypeRentalAgreement,
        types.SecureValueTypeTemporaryRegistration,
        types.SecureValueTypeUtilityBill
    ],
    pydantic.Field(discriminator='QUALNAME')
]
