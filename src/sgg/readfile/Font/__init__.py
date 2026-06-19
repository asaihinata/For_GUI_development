"""フォントファイルのデータを取得するモジュール"""

from pathlib import Path

from matplotlib.font_manager import FontProperties

__all__ = ["Getfont"]


class Getfont:
    def __init__(self, path):
        self.__path = Path(path)
        if not self.__path.exists() or not self.__path.is_file():
            raise FileNotFoundError("ファイルが存在しません")
        if not self.__path.suffix in [".ttf", ".ttc", ".otf"]:
            raise ValueError("フォントファイルを指定してください")
        self.__properties = FontProperties(fname=self.__path)

    def __fspath__(self):
        return str(self.__path)

    @property
    def properties(self):
        return self.__properties

    @property
    def family(self):
        return self.__properties.get_family()

    @property
    def name(self):
        return self.__properties.get_name()

    @property
    def size(self):
        return self.__properties.get_size()

    @property
    def weight(self):
        return self.__properties.get_weight()

    @property
    def style(self):
        return self.__properties.get_style()
