from typing import Any, Literal, Self, TypeVar, overload

import numpy as np
from numpy._typing import _AnyShape, _DTypeLike, _Shape
from numpy.typing import NDArray

from sgg.typing import Typeaxis

from ..dev import _ArrayCommonMixin

__all__ = ["NPArray"]

HANDLED_FUNCTIONS: dict

def implements(np_function) -> Any:
    """
    numpyの関数を`HANDLED_FUNCTIONS`に登録するデコレータ

    :param np_function: 登録対象のnumpy関数
    :return: デコレータ関数を返す
    """

_ShapeT_co = TypeVar("_ShapeT_co", bound=_Shape, default=_AnyShape, covariant=True)
_DTypeT_co = TypeVar("_DTypeT_co", bound=np.dtype, default=np.dtype, covariant=True)

class NPArray[_ShapeT: _ShapeT_co, _Dtypes: _DTypeT_co](
    _ArrayCommonMixin, np.ndarray[_ShapeT, _Dtypes]
):
    """`np.ndarray`を継承した型付き配列クラス"""

    _element_type: None
    _default_dtype: Literal["object"]
    @overload
    def __new__(
        cls,
        data: _ShapeT,
        dtype: None = None,
        *,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPArray[_ShapeT, _Dtypes]: ...
    @overload
    def __new__[ScalarT: np.generic](
        cls,
        data: _ShapeT,
        dtype: _DTypeLike[ScalarT],
        *,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPArray[_ShapeT, ScalarT]: ...
    @overload
    def __new__[ScalarT](
        cls,
        data: _ShapeT,
        dtype: ScalarT,
        *,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPArray[_ShapeT, np.dtype[ScalarT]]: ...
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

    @classmethod
    def full(
        cls, fill_value: Any, shape: _AnyShape, dtype: _Dtypes | None = None
    ) -> NPArray[_AnyShape, _Dtypes]:
        """指定された形状と配列の型を,fill_valueで埋める"""

    @classmethod
    def sequential(cls, shape: _AnyShape) -> NPArray[_AnyShape, np.dtype[np.uint64]]:
        """
        連続した整数値を要素に持つ配列を生成する

        :param shape: 生成する配列の形状。各要素は正の整数でなければならない。
        :type shape: _AnyShapeT
        :returns: 連続値を持つ`NPArray`の配列
        :rtype:
        :raises ShapeError: `shape`が正の整数のみで構成されていない場合に発生させる
        """

    def __class_getitem__(
        cls, item: Any
    ) -> type[NPArray[_ShapeT, np.dtype[_Dtypes]]]: ...
    def __array_ufunc__(
        self,
        ufunc: np.ufunc,
        method: str,
        *inputs: Any,
        **kwargs: Any,
    ) -> NPArray | Any:
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
    def __array__[_ShapeT](
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

    def __ne__(self, value: Any) -> NPArray[Any, np.dtype[np.bool_]]: ...
    def __eq__(self, value: Any) -> NPArray[Any, np.dtype[np.bool_]]: ...
    @property
    def element_type(self) -> None:
        """NPArrayで許可されている型を取得する"""

    def count_nonzero(
        self, axis: Typeaxis = None, keepdims: bool = False
    ) -> np.intp | NDArray[np.intp]:
        """
        0以外の要素の数を数える

        :param axis: 要素を数える軸を指定する
        :type axis: Typeaxis
        :param keepdims: 要素の数を数えた戻り値をサイズ1の次元にするか指定する。
        :type keepdims: bool
        """

    def EType(self) -> NPArray[_ShapeT, np.dtype[object]]:
        """配列内の要素の型を調べる"""

    def numandserial(self) -> NPArray[_ShapeT, np.dtype[np.uint64 | np.number]]:
        """
        配列の`dtype`が数値型場合そのままの配列を返す。

        配列の`dtype`が数値型でない場合は連番を作成し返す。
        """
