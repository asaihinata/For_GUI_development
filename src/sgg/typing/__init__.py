"""フレームワーク全体で使用する型を設定しているモジュール"""

from numpy import datetime64, issubdtype
from numpy._typing._char_codes import _DT64Codes


def serchDtype(dtype="datetime64[D]"):
    if issubdtype(dtype, datetime64) or dtype in _DT64Codes:
        return dtype
    return "datetime64[D]"
