"""外部ライブラリがインストールされているか調べるモジュール"""

from importlib.util import find_spec

__all__ = ["_Required_serch"]

Required_dict = {
    "cycler": "cycler",
    "japanize_matplotlib": "japanize_matplotlib",
    "matplotlib": "matplotlib",
    "numpy": "numpy",
    "Pillow": "PIL",
    "python-dateutil": "dateutil",
    "Requests": "requests",
    "setuptools": "setuptools",
    "validators": "validators",
}


def _Required_serch():
    for k, v in Required_dict.items():
        if find_spec(v) is None:
            raise ImportError(f"{k}がインストールされていません")
