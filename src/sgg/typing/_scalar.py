from datetime import date, datetime, timedelta
from typing import Literal, SupportsComplex, SupportsFloat, SupportsInt

import numpy as np

__all__ = [
    "_BoolScalar",
    "_ComparisonType",
    "_DateArangeScalar",
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
type _NumberScalar = SupportsInt | SupportsFloat | SupportsComplex | np.number | _BoolScalar
type _DateArangeScalar = Literal[
    "TODAY", "today", "NOW", "now"
] | str | np.str_ | datetime | date | np.datetime64
type _TD64Like_co = timedelta | _IntLike_co
type _ComparisonType = np._SupportsGT | np.datetime64 | np._ArrayLikeDT64_co | np._NestedSequence[
    np._SupportsGT
]
