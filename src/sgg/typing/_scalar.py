from datetime import date, datetime

import numpy as np

__all__ = [
    "_BoolScalar",
    "_DateParseScalar",
]
type _BoolScalar = bool | np.bool | np.bool_
type _DateParseScalar = (str | np.str_ | datetime | date | np.datetime64 | int)
