"""基本的な文字列の操作をするモジュール"""

from typing import Any, overload

import numpy as np
import numpy._typing as npt
from numpy import bytes_, str_
from numpy.dtypes import StringDType

import sgg.typing as sgt

from ..dev import _ArrayCommonMixin
from ..npbool import NPBool
from ..npnumber import NPNumber

__all__ = ["NPString"]

class NPString(_ArrayCommonMixin, np.ndarray):
    _element_type: tuple[
        type[str], type[bytes], type[str_], type[bytes_], type[StringDType]
    ]
    _default_dtype: type[str_]
    @overload
    def __new__(
        cls,
        data: sgt._ArrayLikeString_co,
        /,
        dtype: sgt._StringsDTypeLike | None = None,
        *,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPString:
        """
        新しい配列オブジェクトインスタンスを生成する

        :param data: 変換する配列を指定する
        :type data: 任意のstr型もしくはbytes型(dtype)を持つ配列のようなオブジェクト
        :param dtype: 配列に使用するデータ型を指定する
        :type dtype: str | np.str_ | np.bytes_ | bytes | np.dtypes.StringDType
        :param min_ndim: 許容する最小次元数を指定する
        :type min_ndim: int | None
        :param max_ndim: 許容する最大次元数を指定する
        :type max_ndim: int | None
        :param copy: `data`から独立したコピーを作成するか指定する
        :type copy: bool
        :raises ValueError: 次元数が範囲外の場合に発生させる
        :raises TypeError: 要素型が`_element_type`と一致しない場合に発生させる
        """

    @overload
    def __new__(
        cls,
        data: sgt._ArrayLikeString_co,
        /,
        dtype: sgt._StringsDTypeLike | None = None,
        *,
        d_ndim: int | None = None,
        copy: bool = True,
    ) -> NPString:
        """
        新しい配列オブジェクトインスタンスを生成する

        :param data: 変換する配列を指定する
        :type data: 任意のstr型もしくはbytes型(dtype)を持つ配列のようなオブジェクト
        :param dtype: 配列に使用するデータ型を指定する
        :type dtype: str | np.str_ | np.bytes_ | bytes | np.dtypes.StringDType
        :param d_ndim: 固定される次元数を指定する
        :type d_ndim: int | None
        :param copy: `data`から独立したコピーを作成するか指定する
        :type copy: bool
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

    def __eq__(self, value: Any) -> NPBool: ...
    def __ne__(self, value: Any) -> NPBool: ...
    def __add__(self, value: npt._ArrayLikeString_co) -> NPString: ...
    __iadd__ = __add__
    __radd__ = __add__
    def __mul__(self, i: npt._ArrayLikeInt_co) -> NPString:
        """
        配列内の要素を`i`回付け加える

        :param i: 付け加える回数を指定する
        :type i: int
        """
    __imul__ = __mul__
    __rmul__ = __mul__

    @property
    def element_type(
        self,
    ) -> tuple[type[str], type[bytes], type[str_], type[bytes_], type[StringDType]]:
        """NPStringで許可されている型を取得する"""

    def append(self, value: npt._ArrayLikeString_co) -> NPString:
        """配列内の要素の文字に`val`を付け加える"""

    @property
    def low(self) -> NPString:
        """`NPString`内の要素のアルファベットを小文字に変換する"""

    @property
    def up(self) -> NPString:
        """`NPString`内の要素のアルファベットを大文字に変換する"""

    def lower(self) -> NPString:
        """`NPString`内の要素のアルファベットを小文字に変換する"""

    def upper(self) -> NPString:
        """`NPString`内の要素のアルファベットを大文字に変換する"""

    def stringlen(self) -> NPNumber:
        """配列内の要素の文字の長さを求める"""

    def str_len(self) -> NPNumber:
        """配列内の要素の文字の長さを求める"""

    def max(self) -> np.uint64:
        """配列内の要素の文字列の長さが最も長い数値を求める"""

    def min(self) -> np.uint64:
        """配列内の要素の文字列の長さが最も短い数値を求める"""

    def replace(
        self,
        old: sgt._ArrayLikeString_co,
        new: sgt._ArrayLikeString_co,
    ) -> NPString:
        """`NPString`内の要素の文字列の`old`を`new`に置き換える"""

    def slices(
        self,
        start: npt._ArrayLikeInt_co | None = None,
        stop: npt._ArrayLikeInt_co | np._NoValueType | None = None,
        step: npt._ArrayLikeInt_co | None = None,
    ) -> NPString:
        """
        文字列を`start`,`stop`,`step`で指定されたスライスに分割する

        :param start: スライスをする開始する位置を指定する
        :type start: _ArrayLikeInt_co | None
        :param stop: スライスをする終了する位置を指定する
        :type stop: _ArrayLikeInt_co | np._NoValueType | None
        :param step: スライスするステップ数を指定する
        :type step: _ArrayLikeInt_co | None
        """

    def strip(
        self,
        chars: sgt._ArrayLikeString_co | None = None,
    ) -> NPString:
        """
        配列の各要素について,先頭と末尾の文字を取り除いた配列を返す

        :param chars: 削除する文字を指定する
        :type chars: _ArrayLikeString_co | None
        """

    def center(
        self, width: npt._ArrayLikeInt_co, fillchar: sgt._ArrayLikeString_co = " "
    ) -> NPString:
        """
        長さと`width`の幅内で中央寄せされた配列を返す

        :param width: 結果として得られる文字列の長さを指定する
        :type width: _ArrayLikeInt_co
        :param fillchar: 使用する余白の文字を指定する
        :type fillchar: _ArrayLikeString_co
        """

    def left(
        self, width: npt._ArrayLikeInt_co, fillchar: sgt._ArrayLikeString_co = " "
    ) -> NPString:
        """
        長さと`width`の幅内で左寄せされた配列を返す

        :param width: 結果として得られる文字列の長さを指定する
        :type width: _ArrayLikeInt_co
        :param fillchar: 使用する余白の文字を指定する
        :type fillchar: _ArrayLikeString_co
        """

    def right(
        self, width: npt._ArrayLikeInt_co, fillchar: sgt._ArrayLikeString_co = " "
    ) -> NPString:
        """
        長さと`width`の幅内で右寄せされた配列を返す

        :param width: 結果として得られる文字列の長さを指定する
        :type width: _ArrayLikeInt_co
        :param fillchar: 使用する余白の文字を指定する
        :type fillchar: _ArrayLikeString_co
        """

    def zerofill(self, width: npt._ArrayLikeInt_co) -> NPString:
        """
        数値文字列の左側を0で埋めて返します。

        :param width: 0で埋める数を指定する
        :type width: _ArrayLikeInt_co
        """

    def expandtabs(self, tabsize: npt._ArrayLikeInt_co = 8) -> NPString:
        """
        各文字列要素について,すべてのタブを1つ以上のスペースに置き換えた配列を返す

        :param tabsize: タブを置き換えたいスペースの数を指定する
        :type tabsize: _ArrayLikeInt_co
        """

    def endswith(
        self,
        suffix: sgt._ArrayLikeString_co,
        start: npt._ArrayLikeInt_co = 0,
        end: npt._ArrayLikeInt_co | None = None,
    ) -> NPBool:
        """
        配列の要素が`suffix`で終わるかを調べる

        :param suffix: 終了する単語を指定する
        :type suffix: _ArrayLikeString_co
        :param start: 比較を開始する位置を指定する
        :type start: _ArrayLikeInt_co
        :param end: 比較を終える位置を指定する
        :type end: _ArrayLikeInt_co | None
        """

    def startswith(
        self,
        prefix: sgt._ArrayLikeString_co,
        start: npt._ArrayLikeInt_co = 0,
        end: npt._ArrayLikeInt_co | None = None,
    ) -> NPBool:
        """
        配列の要素が`prefix`で始まるかを調べる

        :param prefix: 終了する単語を指定する
        :type prefix: _ArrayLikeString_co
        :param start: 比較を開始する位置を指定する
        :type start: _ArrayLikeInt_co
        :param end: 比較を終える位置を指定する
        :type end: _ArrayLikeInt_co | None
        """

    def capitalize(self) -> NPString:
        """各要素の最初の文字のみを大文字にしたコピーを返します。"""

    def title(self) -> NPString:
        """文字列を要素ごとにタイトルケースに変換する"""

    def decode(
        self,
        encoding: str | None = None,
        errors: str | None = None,
    ) -> NPString:
        """
        要素ごとに`bytes.decode`を呼び出す

        :param encoding: エンコード文字を指定する
        :type encoding: str | None
        :param errors: エンコードエラーの処理方法を指定する
        :type errors: str | None
        """

    def encode(
        self,
        encoding: str | None = None,
        errors: str | None = None,
    ) -> NPString:
        """
        要素ごとに`str.encode`を呼び出す

        :param encoding: エンコード文字を指定する
        :type encoding: str | None
        :param errors: エンコードエラーの処理方法を指定する
        :type errors: str | None
        """

    def istitle(self) -> NPBool:
        """
        要素がタイトルケースの文字列であり,かつ少なくとも1文字が含まれている場合は,各要素に対して`True`を返す。

        そうでない場合は`False`を返す。
        """

    def isnumeric(self) -> NPBool:
        """
        各要素について,その要素が数値のみが含まれている場合は`True`を返す。

        そうでない場合は`False`を返す。
        """

    def isalnum(self) -> NPBool:
        """
        各要素内の文字列のすべての文字が英数字であり,かつ少なくとも1文字が含まれている場合は,各要素に対して`True`を返す。

        そうでない場合は`False`を返す。
        """

    def isspace(self) -> NPBool:
        """
        各要素内の文字列内に空白文字のみが存在し,かつ少なくとも1文字が含まれている場合は,各要素に対して`True`を返す。

        そうでない場合は`False`を返す。
        """

    def isdecimal(self) -> NPBool:
        """
        各要素内の文字列がすべて10進数文字であり,かつ少なくとも1文字が含まれている場合は,各要素に対して`True`を返す。

        そうでない場合は`False`を返す。
        """

    def isupper(self) -> NPBool:
        """
        各要素内の文字列内のすべての文字が大文字であり,かつ少なくとも1文字が含まれている場合は,各要素に対して`True`を返す。

        そうでない場合は`False`を返す。
        """

    @classmethod
    def randombytes(
        cls,
        length: int,
        seed: sgt._Seed = None,
    ) -> NPString:
        """
        指定された長さのランダムに生成されたバイト列を作成する

        :param length: 生成するバイト列の長さを指定する
        :type length: int
        :param seed: 乱数のシード値を指定する
        :raises TypeError: `length`にint型以外を指定した場合に発生させる
        :raises ValueError: `length`に1未満の整数を指定した場合に発生させる
        """

HANDLED_FUNCTIONS: dict

def implements(np_function) -> Any:
    """
    numpyの関数を`HANDLED_FUNCTIONS`に登録するデコレータ

    :param np_function: 登録対象のnumpy関数
    :return: デコレータ関数を返す
    """
