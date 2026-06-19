"""csvファイルのデータを取得するモジュール"""

from pathlib import Path

from polars import read_csv

__all__ = ["Getcsv"]


class Getcsv:
    def __init__(self, path, *, has_header=True, separator=",", encoding="utf-8-sig"):
        self.__path = Path(path)
        if not self.__path.exists() or not self.__path.is_file():
            raise FileNotFoundError("ファイルが存在しません")
        if self.__path.suffix != ".csv":
            raise ValueError("csvファイルを指定してください")
        self.__csv_data = read_csv(
            self.__path, has_header=has_header, separator=separator, encoding=encoding
        )

    def __fspath__(self):
        return str(self.__path)

    @property
    def csv(self):
        return self.__csv_data

    def get_csv(self):
        return self.__csv_data

    @property
    def tonp(self):
        return self.__csv_data.to_numpy()

    def get_numpy(self):
        return self.__csv_data.to_numpy()
