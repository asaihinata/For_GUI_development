from datetime import date, datetime

import numpy as np

__all__ = [
    "_BoolScalar",
    "_DateParseScalar",
    "_NumberScalar",
    "_StrScalar",
    "_IntLike_co",
    "_TD64Like_co",
    "_UIntLike_co",
    "_IntsLike_co",
    "_FloatLike_co"
]
type _BoolScalar = bool | np.bool | np.bool_
type _UIntLike_co = _BoolScalar | np.unsignedinteger
type _IntLike_co = int | np.integer | _BoolScalar
type _IntsLike_co = np.unsignedinteger |_IntLike_co
type _FloatLike_co = float | np.floating | _IntsLike_co
type _NumberScalar = int | float | complex | np.number | _BoolScalar
type _StrScalar = str | bytes | np.character | np.flexible
type _DateParseScalar = str | np.str_ | datetime | date | np.datetime64 | int
type _TD64Like_co = np.timedelta64 | _IntLike_co
