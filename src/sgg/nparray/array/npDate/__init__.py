"""numpyの時間に関する操作をするモジュール"""
from .npdates import NPDate
from .npformatdate import NPFormatDate
print(type(NPFormatDate))
__all__ = ["NPDate", "NPFormatDate"]
