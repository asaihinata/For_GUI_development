"""フレームワークやプログラムのテスト用の値を保存するモジュール"""

from ._dtype import *
from ._timezone import testing_timezone

__all__ = ["testing_timezone"]+getattr(_dtype, "__all__", [])
