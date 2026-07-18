from typing import Any

import numpy as np
from numpy._typing._dtype_like import _SupportsDType

__all__ = ["NumericDTypeLike"]
type NumericDTypeLike = (
    type[bool]
    | type[int]
    | type[float]
    | type[complex]
    | np.dtype[np.bool_ | np.number[Any]]
    | _SupportsDType[np.dtype[np.bool_ | np.number[Any]]]
    | str
)
