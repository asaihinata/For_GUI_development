from datetime import date, datetime

import numpy as np

__all__ = ["DateParseScalar"]
type DateParseScalar = (
    str | bytes | np.str_ | np.bytes_ | datetime | date | np.datetime64 | int
)
