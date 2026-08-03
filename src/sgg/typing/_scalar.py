from typing import SupportsInt,SupportsFloat,SupportsComplex,TypeVar
from datetime import date, datetime, timedelta

import numpy as np

__all__ = [
    "_Arange_Number",
    "_BoolScalar",
    "_BytesScalar",
    "_DateArangeScalar",
    "_DateParseScalar",
    "_FloatLike_co",
    "_IntLike_co",
    "_IntsLike_co",
    "_NumberScalar",
    "_StringScalar",
    "_StrScalar",
    "_TD64Like_co",
    "_UIntLike_co",
    "_ScalarT"
]
type _Arange_Number = np.integer | np.floating | SupportsInt | SupportsFloat
type _BoolScalar = bool | np.bool | np.bool_
type _UIntLike_co = _BoolScalar | np.unsignedinteger
type _IntLike_co = SupportsInt | np.integer | _BoolScalar
type _IntsLike_co = np.unsignedinteger | _IntLike_co
type _FloatLike_co = SupportsFloat | np.floating | _IntsLike_co
type _NumberScalar = SupportsInt | SupportsFloat | SupportsComplex | np.number | _BoolScalar
type _StrScalar = str | np.str_
type _BytesScalar = bytes | np.bytes_
type _StringScalar = str | bytes | np.character | np.flexible
type _DateParseScalar = str | np.str_ | datetime | date | np.datetime64 | SupportsInt
type _DateArangeScalar = str | np.str_ | datetime | date | np.datetime64
type _TD64Like_co = timedelta | _IntLike_co
_ScalarT = TypeVar("_ScalarT", bound=np.generic)