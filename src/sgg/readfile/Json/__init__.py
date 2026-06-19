"""jsonファイルのデータを取得するモジュール"""

from pathlib import Path

from ujson import load

__all__ = ["Getjosn"]


class Getjosn:
    def __init__(self, path):
        self.__path = Path(path)
        if not self.__path.exists() or not self.__path.is_file():
            raise FileNotFoundError("ファイルが存在しません")
        if self.__path.suffix != ".json":
            raise ValueError("jsonファイルを指定してください")
        with open(self.__path, "r", encoding="utf-8") as f:
            self.__json_data = load(f)

    def __fspath__(self):
        return str(self.__path)

    @property
    def json(self):
        return self.__json_data

    def get_json(self):
        return self.__json_data
