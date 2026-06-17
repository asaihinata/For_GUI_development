from numpy import ndarray
from numpy._typing import DTypeLike

__all__ = ["baseDtype"]

class baseDtype:
    def __init__(self, arr: ndarray | DTypeLike, dtype: DTypeLike | None) -> None: ...
    def __bool__(self) -> bool: ...
    @property
    def judge(self) -> bool: ...
