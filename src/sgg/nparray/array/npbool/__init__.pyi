from typing import Any, Iterator, Self, TypeVar, overload

import numpy as np
from numpy._typing import _DTypeLikeBool

from sgg.typing import _ArrayLikeBool_co, _ShapeT

from ..dev import _ArrayShapeMixin

__all__ = ["NPBool"]
HANDLED_FUNCTIONS: dict
_DTypeT = TypeVar("_DTypeT", bound=np.dtype, default=np.dtype[np.bool_], covariant=True)

def implements(np_function) -> Any:
    """
    numpyの関数を`HANDLED_FUNCTIONS`に登録するデコレータ

    :param np_function: 登録対象のnumpy関数
    :return: デコレータ関数を返す
    """

class NPBool(_ArrayShapeMixin, np.ndarray[_ShapeT, np.dtype[_DTypeT]]):
    """`np.ndarray`を継承したbool型の配列クラス"""

    _element_type: tuple[type[bool], type[np.bool_], type[np.bool]]
    _default_dtype: type[np.bool_]

    @overload
    def __new__(
        cls,
        data: _ArrayLikeBool_co,
        dtype: None = np.bool_,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
    ) -> NPBool[_ShapeT, np.dtype[np.bool]]: ...
    @overload
    def __new__(
        cls,
        data: _ArrayLikeBool_co,
        dtype: _DTypeLikeBool,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
    ) -> NPBool[_ShapeT, np.dtype[np.bool]]: ...
    def __new__(
        cls,
        data: _ArrayLikeBool_co,
        dtype: _DTypeLikeBool | None = np.bool_,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
    ) -> Self:
        """
        新しい配列オブジェクトインスタンスを生成する

        :param data: 変換する配列を指定する
        :type data: _ArrayLikeBool_co
        :param dtype: 配列の型を指定する
        :type dtype: _DTypeLikeBool | None
        :param d_ndim: 固定される次元数を指定する
        :type d_ndim: int | None
        :param min_ndim: 許容する最小次元数を指定する
        :type min_ndim: int | None
        :param max_ndim: 許容する最大次元数を指定する
        :type max_ndim: int | None
        :return: 生成された配列オブジェクトインスタンスを返す
        :rtype: Self
        :raises ValueError: 次元数が範囲外の場合に発生させる
        :raises TypeError: 要素型が`_element_type`と一致しない場合に発生させる
        """

    def __class_getitem__(cls, item: Any) -> type[NPBool[Any, Any]]: ...
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
        self, dtype: None = None, copy: bool | None = None
    ) -> np.ndarray[np._ShapeT_co,]: ...
    @overload
    def __array__(
        self, dtype: np._DTypeT, copy: bool | None = None
    ) -> np.ndarray[np._ShapeT_co, np._DTypeT]: ...
    @overload
    def __array__(
        self, dtype: np._DTypeT | None, copy: bool | None = None
    ) -> (
        np.ndarray[np._ShapeT_co, np._DTypeT] | np.ndarray[np._ShapeT_co, np._DTypeT_co]
    ): ...
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
    def __iter__(self) -> Iterator[np.ndarray[_ShapeT, _DTypeT]]: ...
    @property
    def element_type(self) -> tuple[type[bool], type[np.bool_], type[np.bool]]:
        """NPBoolで許可されている型を取得する"""

    def all(self) -> bool:
        """全ての要素が`True`かを調べる"""

    def any(self) -> bool:
        """どれかの要素が`True`かを調べる"""

    def inversion(self) -> Self:
        """配列内の真偽値を反転させる"""
