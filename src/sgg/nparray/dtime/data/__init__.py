from ..typing import Dtype
from .constants import *
__all__=['serch_dtype','DTYPE_LIST','DTYPE_SHORT_LIST','DTYPE_DICT']
def serch_dtype(dtype:Dtype='datetime64[D]')->Dtype:
 if dtype in DTYPE_LIST:return dtype
 elif dtype in DTYPE_SHORT_LIST:return DTYPE_DICT.get(dtype)
 return 'datetime64[D]'