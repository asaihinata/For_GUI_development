from datetime import date, datetime
from typing import Any, Iterator, Literal, Self, overload

import numpy as np
from numpy import datetime64
from numpy._typing import _DTypeLikeTD64, _ShapeLike
from numpy.typing import NDArray

from .._typing import _ArrayLikeDateParse_co, _DTypeT, _ShapeT
from ..dev import _ArrayShapeMixin
from ..npbool import NPBool

__all__ = ["NPFormatDate"]
HANDLED_FUNCTIONS: dict

def implements(np_function) -> Any:
    """
    numpyの関数を`HANDLED_FUNCTIONS`に登録するデコレータ

    :param np_function: 登録対象のnumpy関数
    :return: デコレータ関数を返す
    """

class NPFormatDate(_ArrayShapeMixin, np.ndarray[_ShapeT, np.dtype[_DTypeT]]):
    """`np.ndarray`を継承した様々な日付のフォーマットを特定の日付フォーマットに変換する配列クラス"""

    _element_type: tuple[type[np.datetime64], type[datetime], type[date]]
    _default_dtype: Literal["datetime64[D]"]

    # ==========================================================
    # 生成関連
    # ==========================================================
    @overload
    def __new__(
        cls,
        data: _ArrayLikeDateParse_co,
        dtype: None = "datetime64[D]",
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
    ) -> NPFormatDate[datetime64[_ShapeT], np.dtype[datetime64]]: ...
    @overload
    def __new__(
        cls,
        data: _ArrayLikeDateParse_co,
        dtype: type[_DTypeLikeTD64],
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
    ) -> NPFormatDate[datetime64[_ShapeT], np.dtype[_DTypeLikeTD64]]: ...
    def __new__(
        cls,
        data: _ArrayLikeDateParse_co,
        dtype: type[_DTypeLikeTD64] | None = "datetime64[D]",
        yearfirst: bool = ...,
        dayfirst: bool = ...,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
    ) -> Self:
        """
        様々な日付のフォーマットを特定の日付フォーマットに変換する配列オブジェクトインスタンスを生成する

        :param data: 変換する配列を指定する
        :type data: _ArrayLikeDateParse_co
        :param dtype: 配列の型を指定する
        :type dtype: type[_DTypeLikeTD64] | None
        :param yearfirst: 曖昧な3つの整数からなる日付の最初の値を年として解釈するかどうか指定する
        :type yearfirst: bool
        :param dayfirst: 曖昧な3つの整数からなる日付の最初の値を日もしくは月として解釈するかどうか指定する
        :type dayfirst: bool
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

    # ==========================================================
    # クラスメソッド(検証・型解決)
    # (_resolve_dtype, _validate_ndim, _validate_elements は
    #  _ArrayShapeMixin が型定義済みのため省略)
    # ==========================================================

    # ==========================================================
    # numpyプロトコル関連
    # ==========================================================
    def __class_getitem__(cls, item: Any) -> type[NPFormatDate[Any, Any]]: ...
    def __array_ufunc__(
        self,
        ufunc: np.ufunc,
        method: str,
        *inputs: Any,
        **kwargs: Any,
    ) -> NPFormatDate | Any:
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
    ) -> np.ndarray[np._ShapeT_co, np._DTypeT_co]: ...
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

    # ==========================================================
    # 特殊メソッド(演算子・組み込み関数)
    # ==========================================================
    def __ne__(self, other: Any) -> NPBool[Any, np.dtype[np.bool]]: ...
    def __eq__(self, other: Any) -> NPBool[Any, np.dtype[np.bool]]: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def __contains__(self, value: object) -> bool: ...
    def __iter__(self) -> Iterator[np.ndarray[_ShapeT, _DTypeT]]: ...
    def __len__(self) -> int: ...
    def __reversed__(self) -> Self:
        """
        逆順にした新しい配列オブジェクトを返す

        :return: 全軸で反転した配列を返す
        """

    @overload
    def __getitem__(self, key: int) -> Any | None: ...
    @overload
    def __getitem__(self, key: slice) -> np.ndarray | None: ...
    def __getitem__(self, key: int | slice) -> Any | np.ndarray | None:
        """
        インデックスアクセスをカスタマイズする

        intキーの場合は配列を1次元に展開してからアクセスする。
        `-size <= key < size` の範囲内であれば通常のPythonのインデックス規則
        (負のインデックスは末尾からの参照)に従う。この範囲外のインデックスは
        正負を問わずモジュロ演算(`key % size`)によって折り返してアクセスする。
        ただし`key == size`の場合のみ,末尾の要素(`data[size - 1]`)を返す
        特別な扱いとする。

        :param key: インデックスまたはスライスを指定する
        :type key: int | slice
        :return: インデックスに対応する要素を返す
        :rtype: Any | np.ndarray | None
        :raises IndexError: 配列が空の場合に発生させる
        :raises TypeError: `key`に`int`型もしくは`slice`型以外を指定した場合に発生させる
        """

    # ==========================================================
    # プロパティ
    # (element_typeのみNPFormatDate固有のタプル型に絞り込む
    #  ためオーバーライド。data, dtypes, min_ndim, max_ndim は
    #  _ArrayShapeMixin と同一の型のため省略)
    # ==========================================================
    @property
    def element_type(self) -> tuple[type[np.datetime64], type[datetime], type[date]]:
        """NPFormatDateで許可されている型を取得する"""

    # ==========================================================
    # 形状・次元関連
    # (to_1d, roll, rot90 は _ArrayShapeMixin の Self が
    #  NPFormatDate型に解決されるため,ここでのオーバーライドは不要)
    # ==========================================================

    # ==========================================================
    # 型・変換関連
    # (tonumpy, typeconversion は _ArrayShapeMixin が型定義済み
    #  のため省略)
    # ==========================================================

    # ==========================================================
    # 値の検査・集計関連
    # (all_None, any_None, count_nonzero, unique, counts は
    #  Mixin が型定義済みのため省略)
    # ==========================================================