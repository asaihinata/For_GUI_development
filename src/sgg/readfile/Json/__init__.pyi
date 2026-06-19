"""jsonファイルのデータを取得するモジュール"""

from pathlib import Path, PosixPath, WindowsPath
from typing import Any

__all__ = ["Getjosn"]

class Getjosn:
    def __init__(self, path: Path | WindowsPath | PosixPath | str) -> None:
        """
        jsonファイルのデータを取得する

        :param path: jsonファイルのパスを指定する
        :type path: Path | WindowsPath | PosixPath | str
        :raises FileNotFoundError: ファイルが存在しない場合に発生させる
        :raises ValueError: `path`で指定されたパスの拡張子がjsonファイルではない時に発生させる
        """

    def __fspath__(self) -> str: ...
    @property
    def json(self) -> Any:
        """jsonファイルのデータを取得する

        :return: jsonファイルのデータを返す
        :rtype: Any"""

    def get_json(self) -> Any:
        """jsonファイルのデータを取得する

        :return: jsonファイルのデータを返す
        :rtype: Any"""
