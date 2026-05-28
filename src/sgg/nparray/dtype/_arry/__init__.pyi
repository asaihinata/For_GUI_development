import numpy as np
from numpy._typing import DTypeLike
class Arry:
 arr:np.ndarray
 dt:DTypeLike
 bols:bool
 def __init__(
self,
arr:np.ndarray,
dtype:DTypeLike|None
):''':raises TypeError: `arr`にnp.ndarray以外の型を指定した場合に発生させる'''