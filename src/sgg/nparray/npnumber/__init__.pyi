"""基本的な数値の操作をするモジュール"""

from typing import Any, Literal, NoReturn, Sequence, SupportsIndex, overload

import numpy as np
import numpy._typing as npt

import sgg._typing as sgt

from ..dev import _ArrayCommonMixin

__all__ = ["NPNumber"]
type _ToFloat64 = float | np.integer | np.bool
type _SortKind = Literal[
    "Q",
    "quick",
    "quicksort",
    "M",
    "merge",
    "mergesort",
    "H",
    "heap",
    "heapsort",
    "S",
    "stable",
    "stablesort",
]
type TYPEMETHOD = Literal[
    "inverted_cdf",
    "averaged_inverted_cdf",
    "closest_observation",
    "interpolated_inverted_cdf",
    "hazen",
    "weibull",
    "linear",
    "median_unbiased",
    "normal_unbiased",
]

class NPNumber(_ArrayCommonMixin):
    """`np.ndarray`を継承した数値型の配列クラス"""

    __doc__: str
    _element_type: tuple[type[int], type[float], type[complex], type[np.number]]
    _default_dtype: np.float64
    def __new__(
        cls,
        obj: sgt._ArrayLikeNumber_co,
        /,
        dtype: sgt._NumericDTypeLike | None = None,
        *,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPNumber:
        """
        新しい配列オブジェクトインスタンスを生成する

        :param obj: 変換する配列を指定する
        :type obj: 任意の数値型を持つ配列のようなオブジェクト
        :param dtype: 配列に使用するデータ型を指定する
        :type dtype: int | float | complex | np.number
        :param min_ndim: 許容する最小次元数を指定する
        :type min_ndim: int | None
        :param max_ndim: 許容する最大次元数を指定する
        :type max_ndim: int | None
        :param copy: `obj`から独立したコピーを作成するか指定する
        :type copy: bool
        :raises ValueError: 次元数が範囲外の場合に発生させる
        :raises TypeError: 要素型が`_element_type`と一致しない場合に発生させる
        """

    def __new__(
        cls,
        obj: sgt._ArrayLikeNumber_co,
        /,
        dtype: sgt._NumericDTypeLike | None = None,
        *,
        d_ndim: int | None = None,
        copy: bool = True,
    ) -> NPNumber:
        """
        新しい配列オブジェクトインスタンスを生成する

        :param obj: 変換する配列を指定する
        :type obj: 任意の数値型を持つ配列のようなオブジェクト
        :param dtype: 配列に使用するデータ型を指定する
        :type dtype: int | float | complex | np.number
        :param d_ndim: 固定される次元数を指定する
        :type d_ndim: int | None
        :param copy: `obj`から独立したコピーを作成するか指定する
        :type copy: bool
        :raises ValueError: 次元数が範囲外の場合に発生させる
        :raises TypeError: 要素型が`_element_type`と一致しない場合に発生させる
        """

    def __int__(self) -> int | NoReturn: ...
    def __float__(self) -> float | NoReturn: ...
    @overload
    def __eq__(self, value: sgt._ArrayLikeNumber_co | NPNumber) -> sgt.RBool_: ...
    @overload
    def __eq__(self, value: Any) -> NoReturn: ...
    @overload
    def __ne__(self, value: sgt._ArrayLikeNumber_co | NPNumber) -> sgt.RBool_: ...
    @overload
    def __ne__(self, value: Any) -> NoReturn: ...
    @overload
    def __lt__(self, value: sgt._ArrayLikeNumber_co | NPNumber) -> sgt.RBool_: ...
    @overload
    def __lt__(self, value: Any) -> NoReturn: ...
    @overload
    def __le__(self, value: sgt._ArrayLikeNumber_co | NPNumber) -> sgt.RBool_: ...
    @overload
    def __le__(self, value: Any) -> NoReturn: ...
    @overload
    def __gt__(self, value: sgt._ArrayLikeNumber_co | NPNumber) -> sgt.RBool_: ...
    @overload
    def __gt__(self, value: Any) -> NoReturn: ...
    @overload
    def __ge__(self, value: sgt._ArrayLikeNumber_co | NPNumber) -> sgt.RBool_: ...
    @overload
    def __ge__(self, value: Any) -> NoReturn: ...
    @overload
    def __add__(self, value: sgt._ArrayLikeNumber_co) -> NPNumber: ...
    @overload
    def __add__(self, value: Any) -> NoReturn: ...
    __iadd__ = __add__
    __radd__ = __add__
    @overload
    def __sub__(self, value: sgt._ArrayLikeNumber_co) -> NPNumber: ...
    @overload
    def __sub__(self, value: Any) -> NoReturn: ...
    __rsub__ = __sub__
    __isub__ = __sub__
    @overload
    def __mul__(self, value: sgt._ArrayLikeNumber_co) -> NPNumber: ...
    @overload
    def __mul__(self, value: Any) -> NoReturn: ...
    __imul__ = __mul__
    __rmul__ = __mul__
    @overload
    def __truediv__(self, value: sgt._ArrayLikeNumber_co) -> NPNumber: ...
    @overload
    def __truediv__(self, value: Any) -> NoReturn: ...
    __rtruediv__ = __truediv__
    __itruediv__ = __truediv__
    @overload
    def __floordiv__(self, value: sgt._ArrayLikeNumber_co) -> NPNumber: ...
    @overload
    def __floordiv__(self, value: Any) -> NoReturn: ...
    __rfloordiv__ = __floordiv__
    __ifloordiv__ = __floordiv__
    @overload
    def __mod__(self, value: sgt._ArrayLikeNumber_co) -> NPNumber: ...
    @overload
    def __mod__(self, value: Any) -> NoReturn: ...
    __rmod__ = __mod__
    __imod__ = __mod__
    @overload
    def __pow__(self, value: sgt._ArrayLikeNumber_co) -> NPNumber: ...
    @overload
    def __pow__(self, value: Any) -> NoReturn: ...
    __rpow__ = __pow__
    __ipow__ = __pow__
    @overload
    def __divmod__(
        self, value: sgt._ArrayLikeNumber_co
    ) -> tuple[NPNumber, NPNumber]: ...
    @overload
    def __divmod__(self, value: Any) -> NoReturn: ...
    __rdivmod__ = __divmod__
    def __pos__(self) -> NPNumber: ...
    def __neg__(self) -> NPNumber: ...
    def __abs__(self) -> NPNumber: ...
    @overload
    def __getitem__(self, key: sgt._IntScalar) -> np.number:
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
    def __getitem__(self, key: slice) -> npt.NDArray[np.number]:
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
    ) -> tuple[type[int], type[float], type[complex], type[np.number]]:
        """NPNumberで許可されている型を取得する"""

    def count_nonzero(
        self, axis: sgt._ShapeLike | None = None, keepdims: bool = False
    ) -> NPNumber:
        """
        0以外の要素の数を数える

        :param axis: 要素を数える軸を指定する
        :type axis: int | tuple[int, ...] | None
        :param keepdims: 要素の数を数えた戻り値をサイズ1の次元にするか指定する
        :type keepdims: bool
        """

    @property
    def sturgesval(self) -> np.floating:
        """スタージェスの公式を求める"""

    def cussum(self) -> NPNumber:
        """一つ前の元の値との和を求める"""

    def cusdiff(self) -> NPNumber:
        """一つ前の元の値との差を求める"""

    def cusprod(self) -> NPNumber:
        """一つ前の元の値との積を求める"""

    def cusdiv(self) -> NPNumber:
        """一つ前の元の値との除算を求める"""

    def percentile(
        self,
        q: sgt._FloatScalar,
        axis: sgt.Typeaxis = None,
        method: TYPEMETHOD = "linear",
    ) -> NPNumber:
        """
        指定したパーセンタイルを計算する

        :param q: 求めたいパーセンタイル値を指定する
        :type q: float
        :param axis: 計算する軸の方向を指定する
        :type axis: int | tuple[int, ...] | None
        :param method: パーセンタイルを推定するために使用する方法を指定する
        :type method: Literal["inverted_cdf", "averaged_inverted_cdf", "closest_observation", "interpolated_inverted_cdf", "hazen", "weibull", "linear", "median_unbiased", "normal_unbiased"]
        """

    def quantile(
        self,
        q: sgt._FloatScalar,
        axis: sgt.Typeaxis = None,
        method: TYPEMETHOD = "linear",
    ) -> NPNumber:
        """
        指定した分位点を計算する

        :param q: 求めたい分位点を指定する
        :type q: float
        :param axis: 計算する軸の方向を指定する
        :type axis: int | tuple[int, ...] | None
        :param method: 分位点を推定するために使用する方法を指定する
        :type method: Literal["inverted_cdf", "averaged_inverted_cdf", "closest_observation", "interpolated_inverted_cdf", "hazen", "weibull", "linear", "median_unbiased", "normal_unbiased"]
        """

    def ratio(self, axis: SupportsIndex | None = None) -> NPNumber:
        """行や列ごとの合計に対する比率を求める"""

    @classmethod
    def zeros(
        cls, shape: SupportsIndex, dtype: sgt._NumericDTypeLike | None = None
    ) -> NPNumber:
        """指定された形状と型の新しい配列を0で埋めた配列を作成する"""

    @classmethod
    def ones(
        cls, shape: SupportsIndex, dtype: sgt._NumericDTypeLike | None = None
    ) -> NPNumber:
        """指定された形状と型の新しい配列を0で埋めた配列を作成する"""

    def zero_check(self) -> sgt.RBool_:
        """要素の数値が0の位置を探す"""

    def IQR(
        self,
        axis: sgt.Typeaxis = None,
        method: TYPEMETHOD = "linear",
    ) -> NPNumber:
        """
        配列の四分位数を求める

        :param axis: 計算する軸の方向を指定する
        :type axis: int | tuple[int, ...] | None
        :param method: 分位点を推定するために使用する方法を指定する
        :type method: Literal["inverted_cdf", "averaged_inverted_cdf", "closest_observation", "interpolated_inverted_cdf", "hazen", "weibull", "linear", "median_unbiased", "normal_unbiased"]
        """

    def isinf(self) -> sgt.RBool_:
        """配列の各要素が正または負の無限大(`np.inf`)かどうかを判定する"""

    def isnan(self) -> sgt.RBool_:
        """配列の各要素がNaN(`np.nan`)であるかを判定する"""

    def isfinite(self) -> sgt.RBool_:
        """配列の各要素が有限かどうかを判定する"""

    def isposinf(self) -> sgt.RBool_:
        """配列の各要素が正の無限大(`+np.inf`)かどうかを判定する"""

    def isreal(self) -> sgt.RBool_:
        """配列の各要素が実数かどうかを判定する"""

    def iscomplexobj(self) -> bool:
        """配列の型が複素数型かどうかを判定する"""

    @overload
    def astype(self, dtype: sgt._NumericDTypeLike, copy: bool = True) -> NPNumber:
        """
        配列の要素の型を変換した新しい配列オブジェクトを生成する

        :param dtype: 変換後に使用するデータ型を指定する
        :type dtype: _NumericDTypeLike
        :param copy: `obj`から独立したコピーを作成するか指定する
        :type copy: bool
        :raises ValueError: 次元数が範囲外の場合に発生させる
        :raises TypeError: 変換後の要素の型がこの配列オブジェクトの`_element_type`と一致しない場合に発生させる
        """

    @overload
    def astype[ScalarT: np.generic](
        self, dtype: sgt._DTypeLike[ScalarT], copy: bool = True
    ) -> npt.NDArray[ScalarT]:
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
    def astype(self, dtype: sgt.DTypeNLike, copy: bool = True) -> npt.NDArray[Any]:
        """
        配列の要素の型を変換した新しい配列オブジェクトを生成する

        :param dtype: 変換後に使用するデータ型を指定する
        :type dtype: DTypeLike | None
        :param copy: `obj`から独立したコピーを作成するか指定する
        :type copy: bool
        :raises ValueError: 次元数が範囲外の場合に発生させる
        :raises TypeError: 変換後の要素の型がこの配列オブジェクトの`_element_type`と一致しない場合に発生させる
        """

    def sorts(
        self,
        axis: SupportsIndex | None = -1,
        kind: _SortKind | None = None,
        order: str | Sequence[str] | None = None,
    ) -> NPNumber:
        """
        配列内の数値を並び替える

        :param axis: ソートの基準となる軸を指定する
        :type axis: int | None
        :param kind: ソートアルゴリズムの種類を指定する
        :type kind: Literal["Q", "quick", "quicksort", "M", "merge", "mergesort", "H", "heap", "heapsort", "S", "stable", "stablesort"] | None
        :param order: NPNumberがフィールド定義を持つ配列である場合,どのフィールドを優先して比較するかを指定する
        :type order: str | Sequence[str] | None
        """

    @classmethod
    def sequential(cls, shape: sgt._ShapeInt) -> NPNumber:
        """
        `shape`の形状に沿った連続した整数値の配列を生成する

        :param shape: 配列の形状を指定する
        :type shape: int | tuple[int, ...]
        """

    @classmethod
    def arange(
        cls,
        start: sgt._NumberScalar,
        /,
        stop: sgt._NumberScalar | None = None,
        step: sgt._NumberScalar | None = 1,
        *,
        dtype: sgt._RealNumericDTypeLike | None = None,
    ) -> NPNumber:
        """
        指定された間隔内で等間隔の数値の配列を返す

        :param start: 区間を開始する数値を指定する
        :param stop: 区間を終了する数値を指定する
        :param step: 値の間隔を指定する
        :param dtype: 出力される配列に使用するデータ型を指定する
        """

    @classmethod
    def linspace(
        cls,
        start: sgt._NumberScalar,
        stop: sgt._NumberScalar,
        num: SupportsIndex = 50,
        endpoint: bool = True,
        retstep: Literal[False] = False,
        dtype: sgt._RealNumericDTypeLike | None = None,
        axis: SupportsIndex = 0,
    ) -> NPNumber:
        """
        指定された間隔で等間隔​​の数値の配列を作成する

        :param start: 数列の開始値を指定する
        :param stop:
        シーケンスの終了値を指定する。
        ただし `endpoint`が`False` の場合,生成される値の範囲は`[start,stop)`である。
        `endpoint`が`True` の場合,生成される値の範囲は`[start,stop]`である。

        :param retstep: `retstep`が`True`の場合,戻り値にステップ数を追加する
        :type retstep: bool
        :param num: 生成する値の数を指定する
        :type num: int
        :param endpoint: 生成させる配列の範囲を指定する
        :type endpoint: bool
        :param dtype: 出力する配列に使用するデータ型を指定する
        :type dtype: 実数型
        :param axis: 結果にサンプルを格納する軸を指定する
        :type axis: int
        """

    @classmethod
    def logspace(
        cls,
        start: _ToFloat64,
        stop: _ToFloat64,
        num: SupportsIndex = 50,
        endpoint: bool = True,
        base: _ToFloat64 = 10.0,
        dtype: sgt._RealNumericDTypeLike | None = None,
        axis: SupportsIndex = 0,
    ) -> NPNumber:
        """
        対数スケール上で等間隔に並んだ数値の配列を作成する

        :param start: 数列の開始値を指定する
        :param stop:
        シーケンスの終了値を指定する。
        ただし `endpoint`が`False` の場合,生成される値の範囲は`[start,stop)`である。
        `endpoint`が`True` の場合,生成される値の範囲は`[start,stop]`である。

        :param num: 生成する値の数を指定する
        :type num: int
        :param endpoint: 生成させる配列の範囲を指定する
        :type endpoint: bool
        :param base: 対数の底を指定する
        :param dtype: 出力される配列に使用するデータ型を指定する
        :type dtype: 実数型
        :param axis: 結果を収納する軸を指定する
        :type axis: int
        """

    @classmethod
    def geomspace(
        start: sgt._ArrayLikeComplex_co,
        stop: sgt._ArrayLikeComplex_co,
        num: SupportsIndex = 50,
        endpoint: bool = True,
        dtype: sgt._RealNumericDTypeLike | None = None,
        axis: SupportsIndex = 0,
    ) -> NPNumber:
        """
        対数スケール上で等間隔に配置された(等比数列)配列を作成する

        :param start: 数列の開始値を指定する
        :param stop:
        シーケンスの終了値を指定する。
        ただし `endpoint`が`False` の場合,生成される値の範囲は`[start,stop)`である。
        `endpoint`が`True` の場合,生成される値の範囲は`[start,stop]`である。

        :param num: 生成する値の数を指定する
        :type num: int
        :param endpoint: 生成させる配列の範囲を指定する
        :type endpoint: bool
        :param dtype: 出力される配列に使用するデータ型を指定する
        :type dtype: 実数型
        :param axis: 結果を収納する軸を指定する
        :type axis: int
        """

    @property
    def degree(self) -> NPNumber:
        """角度を弧度法から度数法に変換する"""

    @property
    def deg(self) -> NPNumber:
        """角度を弧度法から度数法に変換する"""

    def deg_to_rad(self) -> NPNumber:
        """角度を弧度法から度数法に変換する"""

    @property
    def radian(self) -> NPNumber:
        """角度を度数法から弧度法に変換する"""

    @property
    def rad(self) -> NPNumber:
        """角度を度数法から弧度法に変換する"""

    def rad_to_deg(self) -> NPNumber:
        """角度を度数法から弧度法に変換する"""

    def dsin(self) -> NPNumber:
        """三角関数の正弦を度数法として要素毎に計算する"""

    def dcos(self) -> NPNumber:
        """三角関数の余弦を度数法として要素毎に計算する"""

    def dtan(self) -> NPNumber:
        """三角関数の正接を度数法として要素毎に計算する"""

    def darcsin(self) -> NPNumber:
        """逆正弦関数の結果を度数法で求める"""

    def darccos(self) -> NPNumber:
        """逆余弦関数の結果を度数法で求める"""

    def dartan(self) -> NPNumber:
        """逆正接関数の結果を度数法で求める"""

    def dtypeinfo(self) -> np.iinfo | np.finfo: ...

    # random
    def choice(
        self,
        size: sgt._ShapeInt | None = None,
        replace: bool = True,
        p: sgt._ArrayLikeFloat_co | None = None,
        axis: int = 0,
        shuffle: bool = True,
        seed: sgt._Seed = None,
    ) -> sgt.RNumber:
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
    def random(
        cls,
        size: sgt._ShapeInt | None = None,
        dtype: sgt._DTypeLikeF64 | sgt._DTypeLikeF32 | None = None,
        seed: sgt._Seed = None,
    ) -> NPNumber:
        """
        [0,1)の範囲でランダムな浮動小数点数の配列を作成する

        :param size: 生成する配列の形状を指定する
        :param dtype: 出力される配列に使用するデータ型を指定する
        :param seed: 乱数のシード値を指定する
        """

    @classmethod
    def uniform(
        cls,
        /,
        low: sgt._FloatScalar = 0.0,
        high: sgt._FloatScalar = 1.0,
        size: sgt._ShapeInt | None = None,
        dtype: sgt._DTypeLikeFloat | None = None,
        seed: sgt._Seed = None,
    ) -> NPNumber:
        """
        一様分布からなる配列を生成する

        :param low: 生成する乱数の下限値を指定する
        :param high: 生成する乱数の上限値を指定する
        :param size: 生成する配列の形状を指定する
        :param dtype: 出力される配列に使用するデータ型を指定する
        :param seed: 乱数のシード値を指定する
        """

    @classmethod
    def normal(
        cls,
        /,
        loc: sgt._FloatScalar = 0.0,
        scale: sgt._FloatScalar = 1.0,
        size: sgt._ShapeInt | None = None,
        dtype: sgt._DTypeLikeFloat | None = None,
        seed: sgt._Seed = None,
    ) -> NPNumber:
        """
        正規分布からなる配列を生成する

        :param loc: 分布の平均値を指定する
        :param scale: 分布の標準偏差を指定する
        :param size: 生成する配列の形状を指定する
        :param dtype: 出力される配列に使用するデータ型を指定する
        :param seed: 乱数のシード値を指定する
        """

    @classmethod
    def integers(
        cls,
        /,
        low: int,
        high: int | None = None,
        size: sgt._ShapeInt | None = None,
        dtype: sgt._DTypeLikeInt | None = np.int64,
        endpoint: bool = False,
        seed: sgt._Seed = None,
    ) -> NPNumber:
        """
        最小値から最大値までの整数の値からなるランダムに生成された配列を作成する

        :param low: 生成される範囲の最小値を指定する
        :param high: 生成される範囲の最大値を指定する
        :param size: 生成する配列の形状を指定する
        :param dtype: 出力される配列に使用するデータ型を指定する
        :param endpoint: 生成される区間の範囲を指定する
        :param seed: 乱数のシード値を指定する
        """

    @classmethod
    def logseries(
        cls,
        /,
        p: sgt._FloatScalar,
        size: sgt._ShapeInt | None = None,
        dtype: sgt._DTypeLikeFloat | None = None,
        seed: sgt._Seed = None,
    ) -> NPNumber:
        """
        対数級数分布からなる配列を生成する

        :param p: 分布の形状を指定する。`p`の範囲は[0,1)である必要がある。
        :param size: 出力する配列の形状を指定する
        :param dtype: 出力される配列に使用するデータ型を指定する
        :param seed: 乱数のシード値を指定する
        """

    def bin(self) -> sgt.RStr:
        """
        整数を\"0b\"が付いた2進数に変換する

        :raises TypeError: `NPNumber`の型が整数型ではない時に発生させる
        :return:
        :rtype: str | NDArray[np.str_]
        """

    def oct(self) -> sgt.RStr:
        """
        整数を\"0x\"が付いた小文字の16進数に変換する

        :raises TypeError: `NPNumber`の型が整数型ではない時に発生させる
        :return:
        :rtype: str | NDArray[np.str_]
        """

    def hex(self) -> sgt.RStr:
        """
        整数を\"0x\"が付いた小文字の16進数に変換する

        :raises TypeError: `NPNumber`の型が整数型ではない時に発生させる
        :return:
        :rtype: str | NDArray[np.str_]
        """

    def tonumpy(self, copy: bool | None = None) -> sgt.NDNumber:
        """配列オブジェクトを`np.ndarray`オブジェクトに変換する"""

    @classmethod
    def full(
        cls,
        fill_value: sgt._NumberScalar,
        shape: sgt._ShapeInt,
        dtype: sgt._NumericDTypeLike = None,
    ) -> NPNumber:
        """
        指定された形状と配列の型で`fill_value`で埋められた配列のオブジェクトを返す

        :param fill_value: 配列内に埋めるスカラー値を指定する
        :type fill_value: _NumberScalar
        :param shape: 配列の形状を指定する
        :type shape: int | tuple[int, ...]
        :param dtype: 配列に使用するデータ型を指定する
        :type dtype: _NumericDTypeLike
        :raises ValueError: `fill_value`にスカラー値で指定しなかった場合に発生させる
        :raises ShapeError: `shape`で正しい値ではない場合に発生させる
        """
    # dtype
    @property
    def types(self) -> type[np.number]: ...
    @property
    def dtypes(self) -> np.dtype[np.number]:
        """インスタンス生成時に確定したdtypeを取得する"""

    @property
    def kinds(self) -> Literal["i", "u", "f", "c"]:
        """配列のデータ型の一般的な種類を識別する文字コードを返す"""

    @property
    def chars(
        self,
    ) -> Literal[
        "h", "H", "i", "I", "l", "L", "q", "Q", "e", "f", "d", "g", "F", "D", "G"
    ]:
        """配列のデータ型固有の文字コードを返す"""

    @property
    def nums(self) -> Literal[3, 4, 5, 6, 7, 8, 9, 10, 23, 11, 12, 13, 14, 15, 16]:
        """配列のデータ型固有の番号を返す"""
