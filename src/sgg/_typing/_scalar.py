from datetime import date, datetime, timedelta
from numbers import Number
from typing import Literal, SupportsComplex, SupportsFloat, SupportsInt

import numpy as np

__all__ = [
    "_BoolScalar",
    "_DateWordScalar",
    "_DT64Scalar",
    "_FloatScalar",
    "_IntScalar",
    "_NumberScalar",
    "_RealNumeric_co",
    "_StringScalar",
    "_TD64Scalar",
]
type _BoolScalar = bool | np.bool | np.bool_
type _IntScalar = int | SupportsInt | np.integer | _BoolScalar
type _FloatScalar = float | SupportsFloat | np.floating | np.unsignedinteger | _IntScalar
type _RealNumeric_co = _FloatScalar
type _NumberScalar = Number | SupportsInt | SupportsFloat | SupportsComplex | np.number | _BoolScalar
type _StringScalar = np.character | str | bytes
type _DateWordScalar = Literal[
    "TODAY", "today", b"TODAY", b"today", "NOW", "now", b"NOW", b"now"
]
type _DT64Scalar = _DateWordScalar | str | np.str_ | datetime | date | np.datetime64
type _TD64Scalar = timedelta | _IntScalar
