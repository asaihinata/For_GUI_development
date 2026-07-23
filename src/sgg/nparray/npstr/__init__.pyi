"""基本的な文字列の操作をするモジュール"""

from types import GenericAlias
from typing import Any, Iterator, Self, TypeVar, overload

import numpy as np
from numpy._typing import (_ArrayLikeAnyString_co, _ArrayLikeBytes_co,
                           _ArrayLikeInt_co, _ArrayLikeStr_co,
                           _ArrayLikeString_co)

from sgg.typing import (Typeaxis, _ArrayLikeAnyString_co, _DTypeLike,
                        _StringDTypeLike, _StringDTypeSupportsArray)

from ..dev import _ArrayCommonMixin
from ..npbool import NPBool
from ..npnumber import NPNumber

__all__ = ["NPString"]
_DType = TypeVar("_DType", bound=np.generic, default=np.dtype[np.str_], covariant=True)

class NPString[_ShapeT: _ArrayLikeAnyString_co, _Dtypes: _DType](
    _ArrayCommonMixin, np.ndarray[_ShapeT, np.dtype[_Dtypes]]
):

    _element_type: tuple[type[str], type[bytes], type[np.str_], type[np.bytes_]]
    _default_dtype: type[np.str_]
    @overload
    def __new__[_ShapeTs, _Dtype](
        cls,
        data: NPString[_ShapeTs, _Dtype],
        /,
        dtype: None = None,
        *,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPString[_ShapeTs, _Dtype]: ...
    @overload
    def __new__[Dtype: _StringDTypeLike](
        cls,
        data: NPString[_ShapeT, _Dtypes],
        /,
        dtype: Dtype,
        *,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPString[_ShapeT, np.dtype[Dtype]]: ...
    @overload
    def __new__(
        cls,
        data: _ShapeT,
        /,
        dtype: None = None,
        *,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPString[_ShapeT, np.dtype[np.str_]]: ...
    @overload
    def __new__[DType: _StringDTypeLike](
        cls,
        data: _ShapeT,
        /,
        dtype: DType,
        *,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPString[_ShapeT, np.dtype[DType]]: ...
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

    def __array_ufunc__(
        self,
        ufunc: np.ufunc,
        method: str,
        *inputs: Any,
        **kwargs: Any,
    ) -> NPString | Any:
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

    @overload
    def __ne__(
        self: NPString[_ShapeT, _ArrayLikeStr_co], value: _ArrayLikeStr_co
    ) -> NPBool[_ShapeT, np.dtype[np.bool_]]: ...
    @overload
    def __ne__(
        self: NPString[_ShapeT, _ArrayLikeBytes_co], value: _ArrayLikeBytes_co
    ) -> NPBool[_ShapeT, np.dtype[np.bool_]]: ...
    @overload
    def __ne__(
        self: NPString[_ShapeT, _ArrayLikeString_co], value: _ArrayLikeString_co
    ) -> NPBool[_ShapeT, np.dtype[np.bool_]]: ...
    @overload
    def __eq__(
        self: NPString[_ShapeT, _ArrayLikeStr_co], value: _ArrayLikeStr_co
    ) -> NPBool[_ShapeT, np.dtype[np.bool_]]: ...
    @overload
    def __eq__(
        self: NPString[_ShapeT, _ArrayLikeBytes_co], value: _ArrayLikeBytes_co
    ) -> NPBool[_ShapeT, np.dtype[np.bool_]]: ...
    @overload
    def __eq__(
        self: NPString[_ShapeT, _ArrayLikeString_co], value: _ArrayLikeString_co
    ) -> NPBool[_ShapeT, np.dtype[np.bool_]]: ...
    @overload
    def __add__(
        self: NPString[_ShapeT, _ArrayLikeStr_co], value: _ArrayLikeStr_co
    ) -> NPString[_ShapeT, np.str_]: ...
    @overload
    def __add__(
        self: NPString[_ShapeT, _ArrayLikeBytes_co], value: _ArrayLikeBytes_co
    ) -> NPString[_ShapeT, np.bytes_]: ...
    @overload
    def __add__(
        self: NPString[_ShapeT, _StringDTypeSupportsArray],
        value: _StringDTypeSupportsArray,
    ) -> NPString[_ShapeT, np.dtypes.StringDType]: ...
    @overload
    def __add__(
        self: NPString[_ShapeT, _ArrayLikeString_co], value: _ArrayLikeString_co
    ) -> (
        NPString[_ShapeT, np.dtype[np.str_]] | NPString[_ShapeT, np.dtypes.StringDType]
    ): ...
    @overload
    def __iadd__(
        self: NPString[_ShapeT, _ArrayLikeStr_co], value: _ArrayLikeStr_co
    ) -> NPString[_ShapeT, np.str_]: ...
    @overload
    def __iadd__(
        self: NPString[_ShapeT, _ArrayLikeBytes_co], value: _ArrayLikeBytes_co
    ) -> NPString[_ShapeT, np.bytes_]: ...
    @overload
    def __iadd__(
        self: NPString[_ShapeT, _StringDTypeSupportsArray],
        value: _StringDTypeSupportsArray,
    ) -> NPString[_ShapeT, np.dtypes.StringDType]: ...
    @overload
    def __iadd__(
        self: NPString[_ShapeT, _ArrayLikeString_co], value: _ArrayLikeString_co
    ) -> (
        NPString[_ShapeT, np.dtype[np.str_]] | NPString[_ShapeT, np.dtypes.StringDType]
    ): ...
    @overload
    def __radd__(
        self: NPString[_ShapeT, _ArrayLikeStr_co], value: _ArrayLikeStr_co
    ) -> NPString[_ShapeT, np.str_]: ...
    @overload
    def __radd__(
        self: NPString[_ShapeT, _ArrayLikeBytes_co], value: _ArrayLikeBytes_co
    ) -> NPString[_ShapeT, np.bytes_]: ...
    @overload
    def __radd__(
        self: NPString[_ShapeT, _StringDTypeSupportsArray],
        value: _StringDTypeSupportsArray,
    ) -> NPString[_ShapeT, np.dtypes.StringDType]: ...
    @overload
    def __radd__(
        self: NPString[_ShapeT, _ArrayLikeString_co], value: _ArrayLikeString_co
    ) -> (
        NPString[_ShapeT, np.dtype[np.str_]] | NPString[_ShapeT, np.dtypes.StringDType]
    ): ...
    def __mul__(self, i: _ArrayLikeInt_co) -> NPString:
        """
        配列内の要素を`i`回付け加える

        :param i: 付け加える回数を指定する
        :type i: _ArrayLikeInt_co
        """

    def __rmul__(self, i: _ArrayLikeInt_co) -> NPString:
        """
        配列内の要素を`i`回付け加える

        :param i: 付け加える回数を指定する
        :type i: _ArrayLikeInt_co
        """

    def __imul__(self, i: _ArrayLikeInt_co) -> NPString:
        """
        配列内の要素を`i`回付け加える

        :param i: 付け加える回数を指定する
        :type i: _ArrayLikeInt_co
        """

    def __iter__(self) -> Iterator[np.ndarray[_ShapeT, _Dtypes]]: ...
    def __class_getitem__(cls, item: Any, /) -> GenericAlias: ...
    @property
    def element_type(
        self,
    ) -> tuple[type[str], type[bytes], type[np.str_], type[np.bytes_]]:
        """NPStringで許可されている型を取得する"""

    def append(self, val: Any) -> NPString:
        """配列内の要素の文字に`val`を付け加える"""

    @property
    def low(self) -> Self:
        """`NPString`内の要素のアルファベットを小文字に変換する"""

    @property
    def up(self) -> Self:
        """`NPString`内の要素のアルファベットを大文字に変換する"""

    def lower(self) -> Self:
        """`NPString`内の要素のアルファベットを小文字に変換する"""

    def upper(self) -> Self:
        """`NPString`内の要素のアルファベットを大文字に変換する"""

    def stringlen(
        self, axis: Typeaxis = None
    ) -> NPNumber[_ShapeT, np.dtype[np.uint64]]:
        """
        配列内の要素の文字の長さを求める

        :param axis: 長さを求める軸を指定する
        :type axis: Typeaxis
        """

    def str_len(self, axis: Typeaxis = None) -> NPNumber[_ShapeT, np.dtype[np.uint64]]:
        """
        配列内の要素の文字の長さを求める

        :param axis: 長さを求める軸を指定する
        :type axis: Typeaxis
        """

    @overload
    def max(self, axis: np._ShapeLike) -> Any:
        """配列内の要素の文字列の長さが最も大きい数値を求める"""

    @overload
    def max(self, axis: Typeaxis = None) -> np.int_:
        """配列内の要素の文字列の長さが最も大きい数値を求める"""

    @overload
    def min(self, axis: np._ShapeLike) -> Any:
        """配列内の要素の文字列の長さが最も大きい数値を求める"""

    @overload
    def min(self, axis: Typeaxis = None) -> np.int_:
        """配列内の要素の文字列の長さが最も小さい数値を求める"""

    def replace(self, old: str, new: str) -> NPString[_ShapeT, _Dtypes]:
        """`NPString`内の要素の文字列の`old`を`new`に置き換える"""

    def center(
        self, width: _ArrayLikeInt_co, fillchar: _ArrayLikeAnyString_co = " "
    ) -> NPString:
        """
        長さと`width`の幅内で中央寄せされた配列を返す

        :param width: 結果として得られる文字列の長さを指定する
        :type width: _ArrayLikeInt_co
        :param fillchar: 使用する余白の文字を指定する
        :type fillchar: _ArrayLikeAnyString_co
        """

    def left(
        self, width: _ArrayLikeInt_co, fillchar: _ArrayLikeAnyString_co = " "
    ) -> NPString:
        """
        長さと`width`の幅内で左寄せされた配列を返す

        :param width: 結果として得られる文字列の長さを指定する
        :type width: _ArrayLikeInt_co
        :param fillchar: 使用する余白の文字を指定する
        :type fillchar: _ArrayLikeAnyString_co
        """

    def right(
        self, width: _ArrayLikeInt_co, fillchar: _ArrayLikeAnyString_co = " "
    ) -> NPString:
        """
        長さと`width`の幅内で右寄せされた配列を返す

        :param width: 結果として得られる文字列の長さを指定する
        :type width: _ArrayLikeInt_co
        :param fillchar: 使用する余白の文字を指定する
        :type fillchar: _ArrayLikeAnyString_co
        """

    def zerofill(self, width: _ArrayLikeInt_co) -> NPString:
        """
        数値文字列の左側を0で埋めて返します。

        :param width: 0で埋める数を指定する
        :type width: _ArrayLikeInt_co
        """

    def expandtabs(self, tabsize: _ArrayLikeInt_co = 4) -> NPString:
        """
        各文字列要素について,すべてのタブを1つ以上のスペースに置き換えた配列を返す

        :param tabsize: タブを置き換えたいスペースの数を指定する
        :type tabsize: _ArrayLikeInt_co
        """

    def endswith(
        self,
        suffix: _ArrayLikeAnyString_co,
        start: _ArrayLikeInt_co = 0,
        end: _ArrayLikeInt_co | None = None,
    ) -> NPBool[_ShapeT, np.dtype[np.bool_]]:
        """
        配列の要素が`suffix`で終わるかを調べる

        :param suffix: 終了する単語を指定する
        :type suffix: _ArrayLikeAnyString_co
        :param start: 比較を開始する位置を指定する
        :type start: _ArrayLikeInt_co
        :param end: 比較を終える位置を指定する
        :type end: _ArrayLikeInt_co | None
        """

HANDLED_FUNCTIONS: dict

def implements(np_function) -> Any:
    """
    numpyの関数を`HANDLED_FUNCTIONS`に登録するデコレータ

    :param np_function: 登録対象のnumpy関数
    :return: デコレータ関数を返す
    """
