from datetime import date, datetime, timedelta
from numbers import Number
from re import Pattern
from typing import Literal, SupportsComplex, SupportsFloat, SupportsInt

import numpy as np

__all__ = [
    "_BoolScalar",
    "_DT64Scalar",
    "_DateWordScalar",
    "_FloatScalar",
    "_IntScalar",
    "_NumberScalar",
    "_PatternStrScalar",
    "_PatternBytesScalar",
    "_RealNumeric_co",
    "_StringScalar",
    "_TD64Scalar",
]
type _BoolScalar = bool | np.bool | np.bool_
type _IntScalar = int | SupportsInt | np.integer | _BoolScalar
type _FloatScalar = (
    float | SupportsFloat | np.floating | np.unsignedinteger | _IntScalar
)
type _RealNumeric_co = _FloatScalar
type _NumberScalar = (
    Number | SupportsInt | SupportsFloat | SupportsComplex | np.number | _BoolScalar
)
type _StringScalar = np.character | str | bytes
type _DateWordScalar = Literal[
    "TODAY", "today", b"TODAY", b"today", "NOW", "now", b"NOW", b"now"
]
type _PatternStrScalar = str | Pattern[str]
type _PatternBytesScalar = bytes | Pattern[bytes]
type _DT64Scalar = _DateWordScalar | str | bytes | np.str_ | np.bytes_ | datetime | date | np.datetime64 | _IntScalar
type _TD64Scalar = timedelta | np.timedelta64 | _IntScalar
