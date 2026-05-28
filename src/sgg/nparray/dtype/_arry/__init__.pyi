import numpy as np
from numpy._typing import DTypeLike
class Arry:
 arr:np.ndarray
 dt:DTypeLike
 def __init__(
self,
arr:np.ndarray,
dtype:np.integer|np.int_|np.uint|np.floating|np.bool_|np.complexfloating|np.str_|np.bytes_|np.datetime64|np.timedelta64
):''':raises TypeError: `arr`にnp.ndarray以外の型を指定した場合に発生させる'''