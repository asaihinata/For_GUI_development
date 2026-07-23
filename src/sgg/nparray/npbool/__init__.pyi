from types import GenericAlias
from typing import Any, Iterator, Self, TypeVar, overload

import numpy as np

from sgg.typing import _ArrayLikeBool_co, _BoolDTypeLike, _DTypeLike

from ..dev import _ArrayCommonMixin

__all__ = ["NPBool"]

_DTypeT = TypeVar("_DTypeT", bound=np.dtype, default=np.dtype[np.bool_], covariant=True)

class NPBool[_ShapeT: _ArrayLikeBool_co, _Dtypes: _DTypeT](
    _ArrayCommonMixin, np.ndarray[_ShapeT, _Dtypes]
):
    """`np.ndarray`を継承したbool型の配列クラス"""

    _element_type: tuple[type[bool], type[np.bool_], type[np.bool]]
    _default_dtype: type[np.bool_]

    @overload
    def __new__(
        cls,
        data: _ShapeT,
        dtype: None = None,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPBool[_ShapeT, np.dtype[np.bool_]]: ...
    @overload
    def __new__[Dtype: _BoolDTypeLike](
        cls,
        data: _ShapeT,
        dtype: Dtype,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPBool[_ShapeT, np.dtype[Dtype]]: ...
    def __new__() -> Self:
        """
        新しい配列オブジェクトインスタンスを生成する

        :param data: 変換する配列を指定する
        :type data: -
        :param dtype: 配列の型を指定する
        :type dtype: -
        :param d_ndim: 固定される次元数を指定する
        :type d_ndim: int | None
        :param min_ndim: 許容する最小次元数を指定する
        :type min_ndim: int | None
        :param max_ndim: 許容する最大次元数を指定する
        :type max_ndim: int | None
        :param copy: `data`から独立したコピーを作成するか指定する
        :type copy: bool
        :return: 生成された配列オブジェクトインスタンスを返す
        :rtype: Self
        :raises ValueError: 次元数が範囲外の場合に発生させる
        :raises TypeError: 要素型が`_element_type`と一致しない場合に発生させる
        """

    def __class_getitem__(cls, item: Any, /) -> GenericAlias: ...
    def __array_ufunc__(
        self,
        ufunc: np.ufunc,
        method: str,
        *inputs: Any,
        **kwargs: Any,
    ) -> NPBool | Any:
        """
        NumPyのufuncの動作をカスタマイズする

        :param ufunc: 呼び出されたufunc
        :type ufunc: np.ufunc
        :param method: 呼び出しメソッド名
        :type method: str
        :param inputs: ufuncへの入力
        :type inputs: Any
        :param kwargs: ufuncへの追加引数
        :type kwargs: Any
        :return: 処理結果を返す
        """

    @overload
    def __array__(
        self, dtype: None = None, /, *, copy: bool | None = None
    ) -> np.ndarray[_ShapeT, _Dtypes]: ...
    @overload
    def __array__[DType: np._dtype | _DTypeLike[np.generic]](
        self, dtype: DType, /, *, copy: bool | None = None
    ) -> np.ndarray[_ShapeT, DType]: ...
    def __array_function__(
        self,
        func: Any,
        types: Any,
        args: tuple,
        kwargs: dict,
    ) -> Any:
        """
        numpy関数の動作をカスタマイズする

        :param func: 呼び出されたnumpy関数
        :type func: Any
        :param types: 関連する型のコレクション
        :type types: Any
        :param args: 位置引数
        :type args: tuple
        :param kwargs: キーワード引数
        :type kwargs: dict
        :return: 演算結果を返す
        :rtype: Any
        """

    def __ne__(self, value: Any) -> NPBool[Any]: ...
    def __eq__(self, value: Any) -> NPBool[Any]: ...
    def __iter__(self) -> Iterator[np.ndarray[_ShapeT, _Dtypes]]: ...
    def __invert__(self) -> Self:
        """配列内の真偽値を反転させる"""

    @property
    def element_type(self) -> tuple[type[bool], type[np.bool_], type[np.bool]]:
        """NPBoolで許可されている型を取得する"""

    def all(self) -> bool:
        """全ての要素が`True`かを調べる"""

    def any(self) -> bool:
        """どれかの要素が`True`かを調べる"""

    def inversion(self) -> Self:
        """配列内の真偽値を反転させる"""

    @property
    def TrueCount(self) -> int:
        """配列内の`True`の数を数える"""

    @property
    def FalseCount(self) -> int:
        """配列内の`False`の数を数える"""

HANDLED_FUNCTIONS: dict

def implements(np_function) -> Any:
    """
    numpyの関数を`HANDLED_FUNCTIONS`に登録するデコレータ

    :param np_function: 登録対象のnumpy関数
    :return: デコレータ関数を返す
    """
