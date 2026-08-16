"""基本的な文字列の操作をするモジュール"""

from typing import Any, Literal, NoReturn, overload

import numpy as np
from numpy import bytes_, str_
from numpy._typing import NDArray, _DTypeLike
from numpy.dtypes import StringDType

import sgg._typing as sgt

from ..dev import _ArrayCommonMixin

__all__ = ["NPString"]

class NPString(_ArrayCommonMixin):
    """`np.ndarray`を継承した文字列型の配列クラス"""

    __doc__: str
    _element_type: tuple[
        type[str], type[bytes], type[str_], type[bytes_], type[StringDType]
    ]
    _default_dtype: str_
    @overload
    def __new__(
        cls,
        obj: sgt._ArrayLikeString_co,
        /,
        dtype: sgt._StringsDTypeLike | None = None,
        *,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPString:
        """
        新しい配列オブジェクトインスタンスを生成する

        :param obj: 変換する配列を指定する
        :type obj: 任意の文字列型かバイト型を持つ配列のようなオブジェクト
        :param dtype: 配列に使用するデータ型を指定する
        :type dtype: str | np.str_ | np.dtypes.StringDType | bytes | np.bytes_ | None
        :param min_ndim: 許容する最小次元数を指定する
        :type min_ndim: int | None
        :param max_ndim: 許容する最大次元数を指定する
        :type max_ndim: int | None
        :param copy: `obj`から独立したコピーを作成するか指定する
        :type copy: bool
        :raises ValueError: 次元数が範囲外の場合に発生させる
        :raises TypeError: 要素型が`_element_type`と一致しない場合に発生させる
        """

    @overload
    def __new__(
        cls,
        obj: sgt._ArrayLikeString_co,
        /,
        dtype: sgt._StringsDTypeLike | None = None,
        *,
        d_ndim: int | None = None,
        copy: bool = True,
    ) -> NPString:
        """
        新しい配列オブジェクトインスタンスを生成する

        :param obj: 変換する配列を指定する
        :type obj: 任意の文字列型かバイト型を持つ配列のようなオブジェクト
        :param dtype: 配列に使用するデータ型を指定する
        :type dtype: str | np.str_ | np.dtypes.StringDType | bytes | np.bytes_ | None
        :param d_ndim: 固定される次元数を指定する
        :type d_ndim: int | None
        :param copy: `obj`から独立したコピーを作成するか指定する
        :type copy: bool
        :raises ValueError: 次元数が範囲外の場合に発生させる
        :raises TypeError: 要素型が`_element_type`と一致しない場合に発生させる
        """

    @overload
    def __eq__(self, value: sgt._ArrayLikeString_co | NPString) -> sgt.RBool_: ...
    @overload
    def __eq__(self, value: Any) -> NoReturn: ...
    @overload
    def __ne__(self, value: sgt._ArrayLikeString_co | NPString) -> sgt.RBool_: ...
    @overload
    def __ne__(self, value: Any) -> NoReturn: ...
    @overload
    def __add__(self, value: sgt._ArrayLikeString_co | NPString) -> NPString: ...
    @overload
    def __add__(self, value: Any) -> NoReturn: ...
    __iadd__ = __add__
    __radd__ = __add__
    @overload
    def __mul__(self, i: sgt._ArrayLikeInt_co) -> NPString:
        """
        配列内の要素を`i`回付け加える

        :param i: 付け加える回数を指定する
        :type i: int
        """

    @overload
    def __mul__(self, i: Any) -> NoReturn: ...
    __imul__ = __mul__
    __rmul__ = __mul__
    @overload
    def __getitem__(self, key: sgt._IntScalar) -> np.character | StringDType:
        """
        インデックスアクセスをカスタマイズする

        intキーの場合は配列を1次元に展開してからアクセスする。
        `-size <= key < size` の範囲内であれば通常のPythonのインデックス規則
        (負のインデックスは末尾からの参照)に従う。この範囲外のインデックスは
        正負を問わずモジュロ演算(`key % size`)によって折り返してアクセスする。
        ただし`key == size`の場合のみ,末尾の要素(`obj[size - 1]`)を返す
        特別な扱いとする。

        :param key: インデックスまたはスライスを指定する
        :type key: int | np.integer
        :raises IndexError: 配列が空の場合に発生させる
        :raises TypeError: `key`に`int`型もしくは`slice`型以外を指定した場合に発生させる
        """

    @overload
    def __getitem__(
        self, key: slice
    ) -> sgt.NDArray[np.character] | sgt._ArrayLikeStringDtype_co:
        """
        インデックスアクセスをカスタマイズする

        intキーの場合は配列を1次元に展開してからアクセスする。
        `-size <= key < size` の範囲内であれば通常のPythonのインデックス規則
        (負のインデックスは末尾からの参照)に従う。この範囲外のインデックスは
        正負を問わずモジュロ演算(`key % size`)によって折り返してアクセスする。
        ただし`key == size`の場合のみ,末尾の要素(`obj[size - 1]`)を返す
        特別な扱いとする。

        :param key: インデックスまたはスライスを指定する
        :type key: slice
        :raises IndexError: 配列が空の場合に発生させる
        :raises TypeError: `key`に`int`型もしくは`slice`型以外を指定した場合に発生させる
        """

    @property
    def element_type(
        self,
    ) -> tuple[type[str], type[bytes], type[str_], type[bytes_], type[StringDType]]:
        """NPStringで許可されている型を取得する"""

    def append(self, value: sgt._ArrayLikeString_co) -> NPString:
        """配列内の要素の文字に`val`を付け加える"""

    @property
    def low(self) -> NPString:
        """NPString内の要素のアルファベットを小文字に変換する"""

    @property
    def up(self) -> NPString:
        """NPString内の要素のアルファベットを大文字に変換する"""

    def lower(self) -> NPString:
        """NPString内の要素のアルファベットを小文字に変換する"""

    def upper(self) -> NPString:
        """NPString内の要素のアルファベットを大文字に変換する"""

    def stringlen(self) -> sgt.RUInt64:
        """配列内の要素の文字の長さを求める"""

    def str_len(self) -> sgt.RUInt64:
        """配列内の要素の文字の長さを求める"""

    def len_max(self) -> np.uint64:
        """配列内の要素の文字列の長さが最も長い数値を求める"""

    def len_min(self) -> np.uint64:
        """配列内の要素の文字列の長さが最も短い数値を求める"""

    @overload
    def replace(
        self,
        old: sgt._ArrayLikeStr_co,
        new: sgt._ArrayLikeStr_co,
    ) -> NPString:
        """
        NPString`内の要素の文字列の`old`を`new`に置き換える

        :param old: 置き換えたいの文字列を指定する
        :type old: 任意のstr型を持つ配列のようなオブジェクト
        :param new: 新しい置換後の文字列を指定する
        :type new: 任意のstr型を持つ配列のようなオブジェクト
        """

    @overload
    def replace(
        self,
        old: sgt._ArrayLikeBytes_co,
        new: sgt._ArrayLikeBytes_co,
    ) -> NPString:
        """
        NPString`内の要素の文字列の`old`を`new`に置き換える

        :param old: 置き換えたいの文字列を指定する
        :type old: 任意のbytes型を持つ配列のようなオブジェクト
        :param new: 新しい置換後の文字列を指定する
        :type new: 任意のbytes型を持つ配列のようなオブジェクト
        """

    @overload
    def replace(self, old: Any, new: Any) -> Any:
        """NPString内の要素の文字列の`old`を`new`に置き換える"""

    def slices(
        self,
        start: sgt._ArrayLikeInt_co | None = None,
        stop: sgt._ArrayLikeInt_co | np._NoValueType | None = None,
        step: sgt._ArrayLikeInt_co | None = None,
    ) -> NPString:
        """
        文字列を`start`,`stop`,`step`で指定されたスライスに分割する

        :param start: スライスをする開始する位置を指定する
        :type start: 整数もしくは整数の配列
        :param stop: スライスをする終了する位置を指定する
        :type stop: 整数もしくは整数の配列
        :param step: スライスするステップ数を指定する
        :type step: 整数もしくは整数の配列
        """

    def strip(
        self,
        chars: sgt._ArrayLikeStrings_co | None = None,
    ) -> NPString:
        """
        配列の各要素について先頭と末尾の文字を取り除いた配列を返す

        :param chars: 削除する文字を指定する
        :type chars: 文字列型もしくはバイト型を持つ配列のようなオブジェクト | None
        """

    def center(
        self, width: sgt._ArrayLikeInt_co, fillchar: sgt._ArrayLikeString_co = " "
    ) -> NPString:
        """
        長さと`width`の幅内で中央寄せされた配列を返す

        :param width: 結果として得られる文字列の長さを指定する
        :type width: 整数もしくは整数の配列
        :param fillchar: 使用する余白の文字を指定する
        :type fillchar: 文字列型もしくはバイト型を持つ配列のようなオブジェクト
        """

    def left(
        self, width: sgt._ArrayLikeInt_co, fillchar: sgt._ArrayLikeString_co = " "
    ) -> NPString:
        """
        長さと`width`の幅内で左寄せされた配列を返す

        :param width: 結果として得られる文字列の長さを指定する
        :type width: 整数もしくは整数の配列
        :param fillchar: 使用する余白の文字を指定する
        :type fillchar: 文字列型もしくはバイト型を持つ配列のようなオブジェクト
        """

    def right(
        self, width: sgt._ArrayLikeInt_co, fillchar: sgt._ArrayLikeString_co = " "
    ) -> NPString:
        """
        長さと`width`の幅内で右寄せされた配列を返す

        :param width: 結果として得られる文字列の長さを指定する
        :type width: 整数もしくは整数の配列
        :param fillchar: 使用する余白の文字を指定する
        :type fillchar: 文字列型もしくはバイト型を持つ配列のようなオブジェクト
        """

    def zerofill(self, width: sgt._ArrayLikeInt_co) -> NPString:
        """
        数値文字列の左側を0で埋めて返す

        :param width: 0で埋める数を指定する
        :type width: 整数もしくは整数の配列
        """

    def expandtabs(self, tabsize: sgt._ArrayLikeInt_co = 8) -> NPString:
        """
        各文字列要素について,すべてのタブを1つ以上のスペースに置き換えた配列を返す

        :param tabsize: タブを置き換えたいスペースの数を指定する
        :type tabsize: 整数もしくは整数の配列
        """

    @overload
    def astype(self, dtype: sgt._StringsDTypeLike, copy: bool = True) -> NPString:
        """
        配列の要素の型を変換した新しい配列オブジェクトを生成する

        :param dtype: 変換後に使用するデータ型を指定する
        :type dtype: _StringsDTypeLike
        :param copy: `obj`から独立したコピーを作成するか指定する
        :type copy: bool
        :raises ValueError: 次元数が範囲外の場合に発生させる
        :raises TypeError: 変換後の要素の型がこの配列オブジェクトの`_element_type`と一致しない場合に発生させる
        """

    @overload
    def astype[ScalarT: np.generic](
        self, dtype: _DTypeLike[ScalarT], copy: bool = True
    ) -> NDArray[ScalarT]:
        """
        配列の要素の型を変換した新しい配列オブジェクトを生成する

        :param dtype: 変換後に使用するデータ型を指定する
        :type dtype: _DTypeLike[ScalarT]
        :param copy: `obj`から独立したコピーを作成するか指定する
        :type copy: bool
        :raises ValueError: 次元数が範囲外の場合に発生させる
        :raises TypeError: 変換後の要素の型がこの配列オブジェクトの`_element_type`と一致しない場合に発生させる
        """

    @overload
    def astype(self, dtype: sgt.DTypeNLike, copy: bool = True) -> NDArray[Any]:
        """
        配列の要素の型を変換した新しい配列オブジェクトを生成する

        :param dtype: 変換後に使用するデータ型を指定する
        :type dtype: DTypeLike | None
        :param copy: `obj`から独立したコピーを作成するか指定する
        :type copy: bool
        :raises ValueError: 次元数が範囲外の場合に発生させる
        :raises TypeError: 変換後の要素の型がこの配列オブジェクトの`_element_type`と一致しない場合に発生させる
        """

    def endswith(
        self,
        suffix: sgt._ArrayLikeString_co,
        start: sgt._ArrayLikeInt_co = 0,
        end: sgt._ArrayLikeInt_co | None = None,
    ) -> sgt.RBool_:
        """
        配列の要素が`suffix`で終わるかを調べる

        :param suffix: 終了する単語を指定する
        :type suffix: 文字列型もしくはバイト型を持つ配列のようなオブジェクト
        :param start: 比較を開始する位置を指定する
        :type start: 整数もしくは整数の配列
        :param end: 比較を終える位置を指定する
        :type end: 整数もしくは整数の配列
        """

    def startswith(
        self,
        prefix: sgt._ArrayLikeString_co,
        start: sgt._ArrayLikeInt_co = 0,
        end: sgt._ArrayLikeInt_co | None = None,
    ) -> sgt.RBool_:
        """
        配列の要素が`prefix`で始まるかを調べる

        :param prefix: 終了する単語を指定する
        :type prefix: 文字列型もしくはバイト型を持つ配列のようなオブジェクト
        :param start: 比較を開始する位置を指定する
        :type start: 整数もしくは整数の配列
        :param end: 比較を終える位置を指定する
        :type end: 整数もしくは整数の配列
        """

    def capitalize(self) -> NPString:
        """各要素の最初の文字のみを大文字にした配列を返す"""

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

    def istitle(self) -> sgt.RBool_:
        """要素がタイトルケースの文字列であり,かつ少なくとも1文字が含まれているかを判定する"""

    def isnumeric(self) -> sgt.RBool_:
        """各要素について,その要素が数値のみが含まれているかを判定する"""

    def isalnum(self) -> sgt.RBool_:
        """各要素内の文字列のすべての文字が英数字であり,かつ少なくとも1文字が含まれているかを判定する"""

    def isspace(self) -> sgt.RBool_:
        """各要素内の文字列内に空白文字のみが存在し,かつ少なくとも1文字が含まれているかを判定する"""

    def isdecimal(self) -> sgt.RBool_:
        """各要素内の文字列がすべて10進数文字であり,かつ少なくとも1文字が含まれているかを判定する"""

    def isupper(self) -> sgt.RBool_:
        """各要素内の文字列内のすべての文字が大文字であり,かつ少なくとも1文字が含まれているかを判定する"""

    def tonumpy(self, copy: bool | None = None) -> sgt.NDString:
        """配列オブジェクトを`np.ndarray`オブジェクトに変換する"""

    @classmethod
    def full(
        cls,
        fill_value: sgt._StringScalar,
        shape: sgt._ShapeInt,
        dtype: sgt._StringsDTypeLike | None = None,
    ) -> NPString:
        """
        指定された形状と配列の型で`fill_value`で埋められた配列のオブジェクトを返す

        :param fill_value: 配列内に埋めるスカラー値を指定する
        :type fill_value: _StringScalar
        :param shape: 配列の形状を指定する
        :type shape: int | tuple[int, ...]
        :param dtype: 配列に使用するデータ型を指定する
        :type dtype: _StringsDTypeLike | None
        :raises ValueError: `fill_value`にスカラー値で指定しなかった場合に発生させる
        :raises ShapeError: `shape`で正しい値ではない場合に発生させる
        """
    # random
    def choice(
        self,
        size: sgt._ShapeInt | None = None,
        replace: bool = True,
        p: sgt._ArrayLikeFloat_co | None = None,
        axis: int = 0,
        shuffle: bool = True,
        seed: sgt._Seed = None,
    ) -> sgt.RString | str:
        """
        配列の要素もしくは軸の配列をランダムに抽選する

        :param size: 出力する配列の形状を指定する
        :type size: int | tuple[int, ...] | None
        :param replace: 抽選する値が復元抽出をするか非復元抽出をするかを指定する
        :type replace: bool
        :param p: 各要素が選ばれる重みを指定する
        :type p: _ArrayLikeFloat_co | None
        :param axis: 選択を行う軸を指定する
        :type axis: int
        :param shuffle: 非復元抽出をする際にサンプルをシャッフルするか指定する
        :type shuffle: bool
        :param seed: 乱数のシード値を指定する
        :type seed: int | SeedSequence | Generator | None
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
    # dtype
    @property
    def types(self) -> type[str_ | bytes_ | StringDType]: ...
    @property
    def dtypes(self) -> np.dtype[str_ | bytes_ | StringDType]:
        """インスタンス生成時に確定したdtypeを取得する"""

    @property
    def kinds(self) -> Literal["S", "U", "T"]:
        """配列のデータ型の一般的な種類を識別する文字コードを返す"""

    @property
    def chars(self) -> Literal["S", "U", "c", "T"]:
        """配列のデータ型固有の文字コードを返す"""

    @property
    def nums(self) -> Literal[18, 19, 2056]:
        """配列のデータ型固有の番号を返す"""
