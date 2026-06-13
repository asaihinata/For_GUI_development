from os.path import isfile
from pathlib import Path

from matplotlib import rcParams
from matplotlib.font_manager import FontProperties, fontManager

__all__ = ["FontFile", "Fontname"]


class FontFile:
    def __init__(
        self, path, style=None, variant=None, weight=None, stretch=None, size=None
    ):
        if isfile(path):
            self.path = Path(path)
            if not self.path.suffix in [".afm", ".otf", ".ttc", ".ttf"]:
                raise ValueError(
                    "ファイルの拡張子がafm,otf,ttc,ttfのどれかではありません"
                )
            self.Properties = FontProperties(
                fname=path,
                style=style,
                variant=variant,
                weight=weight,
                stretch=stretch,
                size=size,
            )
        else:
            self.Properties = FontProperties(
                family=rcParams["font.family"],
                style=style,
                variant=variant,
                weight=weight,
                stretch=stretch,
                size=size,
            )

    def __str__(self):
        return str(self.path)

    def __fspath__(self):
        return self.path


class Fontname:
    name = [i.name for i in fontManager.ttflist]

    def __init__(
        self, family, style=None, variant=None, weight=None, stretch=None, size=None
    ):
        if family in self.name:
            self.Properties = FontProperties(
                family=family,
                style=style,
                variant=variant,
                weight=weight,
                stretch=stretch,
                size=size,
            )
        else:
            self.Properties = FontProperties(
                family=rcParams["font.family"],
                style=style,
                variant=variant,
                weight=weight,
                stretch=stretch,
                size=size,
            )
