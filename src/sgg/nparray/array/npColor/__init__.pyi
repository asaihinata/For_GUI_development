"""
色をデータに変換するモジュール

指定できる形式はRGB,HSL,HEX,カラー名のみ

指定できるカラー名はCSSで指定できる色名  https://drafts.csswg.org/css-color-4/#named-colors
"""

from collections.abc import Iterator
from typing import Any

import numpy as np

from ..nparray import NPArray

__all__ = ["NPColor"]

class NPColor(NPArray):
    def __init__(self, color: str | np.ndarray[str]) -> None:
        """
        色についての配列を作成する

        :param color: 色を指定する
        :type color: str | np.ndarray[str]
        """

    def __repr__(self) -> str: ...
    def __iter__(self) -> Iterator[Any]: ...
    def __getitem__(self, key: int) -> Any: ...
    def tohex(self) -> NPColor:
        """16進数カラーに変換する"""

    def torgba(self) -> NPColor:
        """RGBAに変換する"""

    def torgb(self) -> NPColor:
        """RGBに変換する"""
