"""塗りつぶし領域の領域内のマーカーを設定するモジュール"""

from collections.abc import Iterator
from re import compile

from numpy import all as al, vectorize

from ....nparray import NPString

__all__ = ["Hatch"]


class Hatch(NPString):
    def __new__(cls, hatch: str | tuple[str, ...]) -> None:
        if hatch in ["", None]:
            hatch = [""]
        elif isinstance(hatch, str):
            hatch = [hatch]
        judge = vectorize(lambda x: bool(compile(r"^[/\\|\-+xo*O.]+$").fullmatch(x)))
        datas = super().__new__(cls, hatch, max_ndim=1)
        if al(judge(datas.data)):
            raise ValueError("指定できない値が含まれています")
        return datas

    def __iter__(self) -> Iterator[str]:
        return iter(self.data)

    def __repr__(self) -> str:
        return f"Hatch({self.data})"

    def __getitem__(self, key: int) -> str:
        return super().__getitem__(key)
