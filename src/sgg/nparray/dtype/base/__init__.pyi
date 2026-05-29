import numpy as np
from numpy._typing import DTypeLike
__all__=['baseDtype']
class baseDtype:
 dt:DTypeLike
 bols:bool
 def __init__(
self,
arr:np.ndarray|DTypeLike,
dtype:DTypeLike|None
):...