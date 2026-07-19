from datetime import date, datetime

import numpy as np

__all__ = [
    "BoolScalar",
    "DateParseScalar",
]
type DateParseScalar = (str | np.str_ | datetime | date | np.datetime64 | int)
type BoolScalar = bool | np.bool | np.bool_
