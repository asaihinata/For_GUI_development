"""csvファイルの検索とデータの入手をするモジュール。"""

from csv import reader
from os.path import isfile, join
from pathlib import Path

__all__: list = ["getcsv"]


def getcsv(file: str) -> list[list]:
    """csvファイルが存在するか調べ,そのcsvのデータの入手する。

    :param file: csvファイルのファイル名を指定する。
    :type file: str
    :raises FileNotFoundError: ファイルが存在しない場合に発生させる。
    :raises ValueError: `file`が文字型で指定しなかった場合に発生させる。
    :return: csvファイルのデータを返す。
    :rtype: list[list]"""
    if isinstance(file, str):
        filepath = join(Path(__file__).parent, file)
        if not isfile(filepath):
            raise FileNotFoundError("ファイルが見つかりません。")
        with open(filepath, encoding="utf-8-sig") as f:
            return list(reader(f))
    else:
        raise ValueError("fileが文字型ではありません。")
