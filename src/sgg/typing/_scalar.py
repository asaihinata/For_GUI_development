from datetime import date, datetime, timedelta
from numbers import Number
from typing import Literal, SupportsComplex, SupportsFloat, SupportsInt

import numpy as np

__all__ = [
    "_BoolScalar",
    "_ComparisonType",
    "_DateArangeScalar",
    "_DateWordScalar",
    "_FloatLike_co",
    "_IntLike_co",
    "_NumberScalar",
    "_RealNumeric_co",
    "_TD64Like_co",
]
type _BoolScalar = bool | np.bool | np.bool_
type _IntLike_co = SupportsInt | np.integer | _BoolScalar
type _FloatLike_co = SupportsFloat | np.floating | np.unsignedinteger | _IntLike_co
type _RealNumeric_co = _FloatLike_co
type _NumberScalar = Number | SupportsInt | SupportsFloat | SupportsComplex | np.number | _BoolScalar
type _DateWordScalar = Literal[
    "TODAY", "today", b"TODAY", b"today", "NOW", "now", b"NOW", b"now"
]
type _DateArangeScalar = _DateWordScalar | str | np.str_ | datetime | date | np.datetime64
type _TD64Like_co = timedelta | _IntLike_co
type _ComparisonType = np._SupportsGT | np.datetime64 | np._ArrayLikeDT64_co | np._NestedSequence[
    np._SupportsGT
]
