from typing import Any, Literal, NoReturn, SupportsIndex, overload

import numpy as np
from numpy import datetime64, timedelta64
from numpy._typing import NDArray

import sgg._typing as sgt

from ..dev import _ArrayCommonMixin

__all__ = ["NPDate"]

class NPDate(_ArrayCommonMixin):
    """`np.ndarray`を継承したdatetime64型の配列クラス"""

    __doc__: str
    _element_type: tuple[type[datetime64]]
    _default_dtype: np.dtype[datetime64]
    @overload
    def __new__(
        cls,
        obj: sgt._ArrayLikeDT64_co,
        /,
        dtype: sgt._DtypeLikeDT = "datetime64[D]",
        *,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPDate:
        """
        新しい日付の配列オブジェクトインスタンスを生成する

        :param obj: 変換する配列を指定する
        :type obj: 任意のdatetime64型を持つ配列のようなオブジェクト
        :param dtype: 配列に使用するデータ型を指定する
        :type dtype: datetime64 | _DT64Code_All
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
        obj: Any,
        /,
        dtype: Any | sgt._DtypeLikeDT | None = None,
        *,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NoReturn:
        """
        新しい日付の配列オブジェクトインスタンスを生成する

        :param obj: 変換する配列を指定する
        :type obj: 任意のdatetime64型を持つ配列のようなオブジェクト
        :param dtype: 配列に使用するデータ型を指定する
        :type dtype: Any
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
        obj: sgt._ArrayLikeDT64_co,
        /,
        dtype: sgt._DtypeLikeDT = "datetime64[D]",
        *,
        d_ndim: int | None = None,
        copy: bool = True,
    ) -> NPDate:
        """
        新しい日付の配列オブジェクトインスタンスを生成する

        :param obj: 変換する配列を指定する
        :type obj: 任意のdatetime64型を持つ配列のようなオブジェクト
        :param dtype: 配列に使用するデータ型を指定する
        :type dtype: datetime64 | _DT64Code_All
        :param d_ndim: 固定される次元数を指定する
        :type d_ndim: int | None
        :param copy: `obj`から独立したコピーを作成するか指定する
        :type copy: bool
        :raises ValueError: 次元数が範囲外の場合に発生させる
        :raises TypeError: 要素型が`_element_type`と一致しない場合に発生させる
        """

    @overload
    def __new__(
        cls,
        obj: Any,
        /,
        dtype: Any | sgt._DtypeLikeDT | None = None,
        *,
        d_ndim: int | None = None,
        copy: bool = True,
    ) -> NoReturn:
        """
        新しい日付の配列オブジェクトインスタンスを生成する

        :param obj: 変換する配列を指定する
        :type obj: 任意のdatetime64型を持つ配列のようなオブジェクト
        :param dtype: 配列に使用するデータ型を指定する
        :type dtype: Any
        :param d_ndim: 固定される次元数を指定する
        :type d_ndim: int | None
        :param copy: `obj`から独立したコピーを作成するか指定する
        :type copy: bool
        :raises ValueError: 次元数が範囲外の場合に発生させる
        :raises TypeError: 要素型が`_element_type`と一致しない場合に発生させる
        """

    def __add__(self, value: sgt._ArrayLikeTD64_co) -> NPDate: ...
    __iadd__ = __add__
    __radd__ = __add__
    @overload
    def __sub__(self, value: sgt._ComparisonDT64 | NPDate) -> sgt.RTimedelta64: ...
    @overload
    def __sub__(self, value: sgt._ArrayLikeTD64_co) -> NPDate: ...
    @overload
    def __sub__(self, value: Any) -> NoReturn: ...
    __isub__ = __sub__
    @overload
    def __rsub__(self, value: sgt._ComparisonDT64 | NPDate) -> sgt.RTimedelta64: ...
    @overload
    def __rsub__(self, value: Any) -> NoReturn: ...
    @overload
    def __eq__(self, value: sgt._ComparisonDT64 | NPDate) -> sgt.RBool_: ...
    @overload
    def __eq__(self, value: None = None) -> sgt.RBool_: ...
    @overload
    def __eq__(self, value: Any) -> NoReturn: ...
    @overload
    def __ne__(self, value: sgt._ComparisonDT64 | NPDate) -> sgt.RBool_: ...
    @overload
    def __ne__(self, value: None = None) -> sgt.RBool_: ...
    @overload
    def __ne__(self, value: Any) -> NoReturn: ...
    @overload
    def __lt__(self, value: sgt._ComparisonDT64 | NPDate) -> sgt.RBool_: ...
    @overload
    def __lt__(self, value: Any) -> NoReturn: ...
    @overload
    def __le__(self, value: sgt._ComparisonDT64 | NPDate) -> sgt.RBool_: ...
    @overload
    def __le__(self, value: Any) -> NoReturn: ...
    @overload
    def __gt__(self, value: sgt._ComparisonDT64 | NPDate) -> sgt.RBool_: ...
    @overload
    def __gt__(self, value: Any) -> NoReturn: ...
    @overload
    def __ge__(self, value: sgt._ComparisonDT64 | NPDate) -> sgt.RBool_: ...
    @overload
    def __ge__(self, value: Any) -> NoReturn: ...
    @overload
    def __getitem__(self, key: sgt._IntScalar) -> datetime64:
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
    def __getitem__(self, key: slice) -> sgt.NDArray[datetime64]:
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

    @overload
    def __getitem__(self, key: Any) -> Any: ...
    # property
    @property
    def element_type(self) -> type[datetime64]:
        """NPDateで許可されている型を取得する"""
    # 日付
    @property
    def year(self) -> sgt.RInt64:
        """配列の年を返す"""

    @property
    def month(self) -> sgt.RInt8:
        """配列の月を返す"""

    @property
    def day(self) -> sgt.RUInt8:
        """配列の日付を返す"""
    # 判定
    def isnat(self) -> sgt.RBool_:
        """要素が欠損(Nat)かを判定する"""
    # 変換
    def astype(self, dtype: sgt._DtypeLikeDT, copy: bool = True) -> NPDate:
        """
        配列の要素の型を変換した新しい配列オブジェクトを生成する

        :param dtype: 変換後に使用するデータ型を指定する
        :type dtype: _DtypeLikeDT
        :param copy: `obj`から独立したコピーを作成するか指定する
        :type copy: bool
        :raises ValueError: 次元数が範囲外の場合に発生させる
        :raises TypeError: 変換後の要素の型がこの配列オブジェクトの`_element_type`と一致しない場合に発生させる
        """

    @overload
    def astype[ScalarT: np.generic](
        self, dtype: sgt._DTypeLike[ScalarT], copy: bool = True
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

    def to_datetime(self) -> np.ndarray:
        """配列内の日付を`datetime.datetime`の配列に変換する"""

    def to_date(self) -> np.ndarray:
        """配列内の日付を`datetime.date`の配列に変換する"""

    def to_str(self) -> sgt.RStr_:
        """配列内の日付を文字列型の配列に変換する"""

    def to_timezone(self, timezone: sgt._TypeTimezone, /) -> NPDate:
        """配列内の日付のタイムゾーンを指定したタイムゾーン(`timezone`)の日付の配列を作成する"""

    def strftime(self, format: str) -> NDArray[np.str_]:
        """日付のフォーマットを別のフォーマットで変換する"""
    # 範囲
    @classmethod
    def arange(
        cls,
        start: sgt._DT64Scalar,
        stop: sgt._DT64Scalar,
        /,
        step: sgt._TD64Scalar | None = 1,
        dtype: sgt._DT64Code_All | None = None,
    ) -> NPDate:
        """
        指定された間隔内で等間隔の日付を返す

        :param start: 区間を開始する日付を指定する
        :type start: Literal["TODAY", "today", "NOW", "now"] | str | np.str_ | datetime | date | np.datetime64
        :param stop: 区間を終了する日付を指定する
        :type stop: Literal["TODAY", "today", "NOW", "now"] | str | np.str_ | datetime | date | np.datetime64
        :param step: 値の間隔を指定する
        :type step: int | bool | np.integer | np.bool | bool | timedelta | np.timedelta64 | None
        :param dtype: 配列に使用するデータ型を指定する
        :type dtype: _DT64Code_All | None
        """

    @overload
    @classmethod
    def linspace(
        cls,
        start: sgt._DT64Scalar,
        stop: sgt._DT64Scalar,
        /,
        num: SupportsIndex = 50,
        endpoint: bool = True,
        retstep: Literal[False] = False,
        dtype: sgt._DT64Code_All = "D",
        axis: SupportsIndex = 0,
    ) -> NPDate:
        """
        指定された間隔で等間隔​​の日付を返します。

        :param start: 区間を開始する日付を指定する
        :type start: Literal["TODAY", "today", "NOW", "now"] | str | np.str_ | datetime | date | np.datetime64
        :param stop: 区間を終了する日付を指定する
        :type stop: Literal["TODAY", "today", "NOW", "now"] | str | np.str_ | datetime | date | np.datetime64
        :param num: 生成する日付の数を指定する
        :type num: int
        :param endpoint: `stop`を結果に含めるか指定する
        :type endpoint: bool
        :param retstep: 計算された間隔を返すか指定する
        :type retstep: bool
        :param dtype: 配列に使用するデータ型を指定する
        :type dtype: _DT64Code_All
        :param axis: 結果にサンプルを格納する軸を指定する
        :type axis: int
        """

    @overload
    @classmethod
    def linspace(
        cls,
        start: sgt._DT64Scalar,
        stop: sgt._DT64Scalar,
        /,
        num: SupportsIndex = 50,
        endpoint: bool = True,
        retstep: Literal[True] = True,
        dtype: sgt._DT64Code_All | None = "D",
        axis: SupportsIndex = 0,
    ) -> tuple[NPDate, timedelta64]:
        """
        指定された間隔で等間隔​​の日付を返します。

        :param start: 区間を開始する日付を指定する
        :type start: Literal["TODAY", "today", "NOW", "now"] | str | np.str_ | datetime | date | np.datetime64
        :param stop: 区間を終了する日付を指定する
        :type stop: Literal["TODAY", "today", "NOW", "now"] | str | np.str_ | datetime | date | np.datetime64
        :param num: 生成する日付の数を指定する
        :type num: int
        :param endpoint: `stop`を結果に含めるか指定する
        :type endpoint: bool
        :param retstep: 計算された間隔を返すか指定する
        :type retstep: bool
        :param dtype: 配列に使用するデータ型を指定する
        :type dtype: _DT64Code_All | None
        :param axis: 結果にサンプルを格納する軸を指定する
        :type axis: int
        """

    def range(self) -> tuple[datetime64, datetime64]:
        """配列内の日付の最小の日付と最大の日付を求める"""
    # 日付差
    def diff_today(self, days: bool = False) -> sgt.RTimedelta64:
        """
        配列内の日付を今日の日にちで引いた配列を求める

        :param days: 今日を含めるか指定する
        :type days: bool
        """

    def diff_tfyear(self) -> sgt.RTimedelta64:
        """配列内の日付の年の開始からの日付の差を求める"""

    def diff_teyear(self) -> sgt.RTimedelta64:
        """配列内の日付の年の終わりからの日付の差を求める"""

    def diff_tfmonth(self) -> sgt.RTimedelta64:
        """配列内の日付の月の開始からの日付の差を求める"""

    def diff_temonth(self) -> sgt.RTimedelta64:
        """配列内の日付の月の終わりからの日付の差を求める"""

    @classmethod
    def today(cls) -> NPDate:
        """現在日付(UTCの日付)を返す"""

    @classmethod
    def now(cls) -> NPDate:
        """現在時刻(UTC時刻)を返す"""

    @classmethod
    def unix(cls) -> NPDate:
        """UTC時刻を返す"""
    # 曜日
    def weekday(self) -> sgt.RUInt8:
        """その日付時刻の曜日をツェラーの公式で求める"""

    def begin_month_weekday(self) -> sgt.RUInt8:
        """その日付時刻の月初の曜日をツェラーの公式で求める"""

    def end_month_weekday(self) -> sgt.RUInt8:
        """その日付時刻の月末の曜日をツェラーの公式で求める"""

    def week_name(self) -> sgt.RStr_:
        """日付の曜日を`%A`のフォーマットで取得する"""
    # 閏年
    def leapyear(self) -> sgt.RBool_:
        """その日付の年が閏年かどうかを判定する"""

    def leapcount(self) -> int:
        """配列内の閏年の数を数える"""
    # dtype
    def dtype_range(self) -> NPDate:
        """現在配列の配列型(`dtype`)で表現できる最大·最小の日付時刻を求める"""

    def dtype_max(self) -> NPDate:
        """現在配列の配列型(`dtype`)で表現できる最大の日付時刻を求める"""

    def dtype_min(self) -> NPDate:
        """現在配列の配列型(`dtype`)で表現できる最小の日付時刻を求める"""

    @classmethod
    def unit_range(cls, unit: sgt._DtypeLikeDT) -> tuple[datetime64, datetime64]:
        """
        日付単位(`unit`)が表現できる範囲の最大·最小の日付時刻を求める

        :param unit: 日付単位を指定する
        :type unit: _DtypeLikeDT
        """

    @classmethod
    def unit_max(cls, unit: sgt._DtypeLikeDT) -> datetime64:
        """
        日付単位(`unit`)が表現できる範囲の最大の日付時刻を求める

        :param unit: 日付単位を指定する
        :type unit: _DtypeLikeDT
        """

    @classmethod
    def unit_min(cls, unit: sgt._DtypeLikeDT) -> datetime64:
        """
        日付単位(`unit`)が表現できる範囲の最小の日付時刻を求める

        :param unit: 日付単位を指定する
        :type unit: _DtypeLikeDT
        """

    def tonumpy(self, copy: bool | None = None) -> sgt.NDDatetime64:
        """配列オブジェクトを`np.ndarray`オブジェクトに変換する"""

    @classmethod
    def full(
        cls,
        fill_value: sgt._DT64Scalar,
        shape: sgt._ShapeInt,
        dtype: sgt._DtypeLikeDT | None = None,
    ) -> NPDate:
        """
        指定された形状と配列の型で`fill_value`で埋められた配列のオブジェクトを返す

        :param fill_value: 配列内に埋めるスカラー値を指定する
        :type fill_value: _DT64Scalar
        :param shape: 配列の形状を指定する
        :type shape: int | tuple[int, ...]
        :param dtype: 配列に使用するデータ型を指定する
        :type dtype: _DtypeLikeDT | None
        :raises ValueError: `fill_value`にスカラー値で指定しなかった場合に発生させる
        :raises ValueError: `dtype`でdatetime64型を指定しなかった場合に発生させる
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
    ) -> sgt.RDatetime64:
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
    # dtype
    @property
    def types(self) -> type[datetime64]: ...
    @property
    def dtypes(self) -> np.dtype[datetime64]:
        """インスタンス生成時に確定したdtypeを取得する"""

    @property
    def dtypeunit(self) -> Literal[sgt._TimeStrUnit, "datetime64"]: ...
    @property
    def kinds(self) -> Literal["M"]:
        """配列のデータ型の一般的な種類を識別する文字コードを返す"""

    @property
    def chars(self) -> Literal["M"]:
        """配列のデータ型固有の文字コードを返す"""

    @property
    def nums(self) -> Literal[21]:
        """配列のデータ型固有の番号を返す"""
