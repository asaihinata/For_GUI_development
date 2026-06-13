from matplotlib.colors import to_hex, to_rgb, to_rgba
import numpy as np

__all__ = ["Color"]


class Color:
    def __init__(self, color, *, default_color="#000000", keep_alpha=False):
        self.default = default_color
        if not isinstance(keep_alpha, bool):
            keep_alpha = False
        else:
            keep_alpha = keep_alpha
        if isinstance(color, Color):
            self.color = color.color
        else:
            if isinstance(color, list | tuple):
                colors = np.array(color)
            elif isinstance(color, str):
                colors = np.array([color.lower()])
            elif isinstance(color, np.ndarray):
                colors = color
            else:
                colors = [None]
            self.color = np.array(
                [self.default if i is None else to_hex(i, keep_alpha) for i in colors],
                dtype=str,
            )

    def tohex(self, keep_alpha=False):
        if not isinstance(keep_alpha, bool):
            keep_alpha = False
        else:
            keep_alpha = keep_alpha
        self.color = np.array(
            [self.default if i is None else to_hex(i, keep_alpha) for i in self.color],
            dtype=str,
        )
        return self

    def torgba(self, alpha=None):
        if alpha is not None:
            if not isinstance(alpha, int | float):
                raise TypeError("alphaは数値の型を指定してください")
            if not 0.0 <= alpha <= 1.0:
                raise ValueError("0.0<=alpha<=1.0の範囲で指定してください")
        self.color = np.array([to_rgba(i, alpha) for i in self.color], dtype=float)
        return self

    def torgb(self):
        self.color = np.array([to_rgb(i) for i in self.color], dtype=float)
        return self

    def __iter__(self):
        return iter(self.color)

    def __contains__(self, item):
        return item in self.color

    def __len__(self):
        return self.color.size

    def __getitem__(self, val):
        if isinstance(val, int):
            if 0 <= val < len(self):
                return self.color[val]
            raise IndexError("配列の範囲外です")
        elif isinstance(val, slice):
            return self.color[val]
        raise TypeError("リストのインデックスはintまたはslicesである必要があります")
