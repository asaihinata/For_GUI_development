"""csvファイルのデータを取得するモジュール"""

from pathlib import Path, PosixPath, WindowsPath
from typing import Any

from numpy import ndarray
from polars import DataFrame
from polars._typing import CsvEncoding

__all__ = ["Getcsv"]

class Getcsv:
    def __init__(
        self,
        path: Path | WindowsPath | PosixPath | str,
        *,
        has_header: bool = True,
        separator: str = ",",
        encoding: CsvEncoding | str = "utf-8-sig",
    ) -> None:
        """
        csvファイルのデータを取得する

        :param path: csvファイルのパスを指定する
        :type path: Path | WindowsPath | PosixPath | str
        :param has_header: 先頭行をヘッターとして扱うか指定する
        :type has_header: bool
        :param separator: 区切り文字を指定する
        :type separator: str
        :param encoding: 文字コードを指定する
        :type encoding: CsvEncoding | str
        :raises FileNotFoundError: ファイルが存在しない場合に発生させる
        :raises ValueError: `path`で指定されたパスの拡張子がcsvファイルではない時に発生させる
        """

    def __fspath__(self) -> str: ...
    @property
    def csv(self) -> DataFrame:
        """:class:`polars.polars`で読み取ったcsvファイルのデータを取得する"""

    def get_csv(self) -> DataFrame:
        """:class:`polars.polars`で読み取ったcsvファイルのデータを取得する"""

    @property
    def tonp(self) -> ndarray[Any, Any]:
        """:class:`polars.polars`で読み取ったcsvファイルのデータをNumPyの`ndarray`として取得する"""

    def get_numpy(self) -> ndarray[Any, Any]:
        """:class:`polars.polars`で読み取ったcsvファイルのデータをNumPyの`ndarray`として取得する"""
