from typing import Any

import numpy as np
from numpy._typing import _SupportsDType,_StrCodes,_DTypeLike

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
type StringDTypeLike=type[str] | _DTypeLike[np.str_] | _StrCodes