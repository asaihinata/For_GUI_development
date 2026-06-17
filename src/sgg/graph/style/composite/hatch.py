"""塗りつぶし領域の領域内のマーカーを設定するモジュール"""

from collections.abc import Iterator
from re import compile

from numpy import all as al, vectorize

from ....nparray import NPString

__all__ = ["Hatch"]


class Hatch(NPString):
    def __init__(self, hatch: str | tuple[str, ...]) -> None:
        if hatch in ["", None]:
            hatch = [""]
        elif isinstance(hatch, str):
            hatch = [hatch]
        super().__init__(hatch, depth_limit=1)
        judge = vectorize(lambda x: bool(compile(r"^[/\\|\-+xo*O.]+$").fullmatch(x)))
        if al(judge(self.data)):
            raise ValueError("指定できない値が含まれています")

    def __iter__(self) -> Iterator[str]:
        return iter(self.data)

    def __repr__(self) -> str:
        return f"Hatch({self.data})"

    def __getitem__(self, key: int) -> str:
        return self.get(key)
