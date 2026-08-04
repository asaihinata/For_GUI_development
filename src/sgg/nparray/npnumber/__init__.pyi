"""基本的な数値の操作をするモジュール"""

from typing import Any, Literal, Sequence, SupportsIndex, overload

import numpy as np
import numpy._typing as npt
from numpy.typing import NDArray

import sgg.typing as sgt

from ..dev import _ArrayCommonMixin
from ..npbool import NPBool

__all__ = ["NPNumber"]
type _ToFloat64 = float | np.integer | np.bool
type _OrderCF = Literal["C", "F"] | None
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

class NPNumber(_ArrayCommonMixin, np.ndarray):
    """`np.ndarray`を継承した数値型の配列クラス"""

    _element_type: tuple[type[int], type[float], type[complex], type[np.number]]
    _default_dtype: type[np.float64]
    def __new__(
        cls,
        data: sgt._ArrayLikeNumber_co,
        /,
        dtype: sgt._NumericDTypeLike | None = None,
        *,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
        copy: bool = True,
    ) -> NPNumber:
        """
        新しい配列オブジェクトインスタンスを生成する

        :param data: 変換する配列を指定する
        :type data: -
        :param dtype: 配列の型を指定する
        :type dtype: dtype
        :param min_ndim: 許容する最小次元数を指定する
        :type min_ndim: int | None
        :param max_ndim: 許容する最大次元数を指定する
        :type max_ndim: int | None
        :param copy: `data`から独立したコピーを作成するか指定する
        :type copy: bool
        :return: 生成された配列オブジェクトインスタンスを返す
        :rtype: NPNumber
        :raises ValueError: 次元数が範囲外の場合に発生させる
        :raises TypeError: 要素型が`_element_type`と一致しない場合に発生させる
        """

    def __new__(
        cls,
        data: sgt._ArrayLikeNumber_co,
        /,
        dtype: sgt._NumericDTypeLike | None = None,
        *,
        d_ndim: int | None = None,
        copy: bool = True,
    ) -> NPNumber:
        """
        新しい配列オブジェクトインスタンスを生成する

        :param data: 変換する配列を指定する
        :type data: -
        :param dtype: 配列の型を指定する
        :type dtype: dtype
        :param d_ndim: 固定される次元数を指定する
        :type d_ndim: int | None
        :param copy: `data`から独立したコピーを作成するか指定する
        :type copy: bool
        :return: 生成された配列オブジェクトインスタンスを返す
        :rtype: NPNumber
        :raises ValueError: 次元数が範囲外の場合に発生させる
        :raises TypeError: 要素型が`_element_type`と一致しない場合に発生させる
        """

    def __array_ufunc__(
        self,
        ufunc: np.ufunc,
        method: str,
        *inputs: Any,
        **kwargs: Any,
    ) -> NPNumber | Any:
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
    def __lt__(self, value: Any) -> NPBool: ...
    def __le__(self, value: Any) -> NPBool: ...
    def __gt__(self, value: Any) -> NPBool: ...
    def __ge__(self, value: Any) -> NPBool: ...
    def __add__(self, value: sgt._NumberScalar) -> NPNumber: ...
    def __radd__(self, value: sgt._NumberScalar) -> NPNumber: ...
    def __iadd__(self, value: sgt._NumberScalar) -> NPNumber: ...
    def __sub__(self, value: sgt._NumberScalar) -> NPNumber: ...
    def __rsub__(self, value: sgt._NumberScalar) -> NPNumber: ...
    def __isub__(self, value: sgt._NumberScalar) -> NPNumber: ...
    def __mul__(self, value: sgt._NumberScalar) -> NPNumber: ...
    def __rmul__(self, value: sgt._NumberScalar) -> NPNumber: ...
    def __imul__(self, value: sgt._NumberScalar) -> NPNumber: ...
    def __truediv__(self, value: sgt._NumberScalar) -> NPNumber: ...
    def __rtruediv__(self, value: sgt._NumberScalar) -> NPNumber: ...
    def __itruediv__(self, value: sgt._NumberScalar) -> NPNumber: ...
    def __floordiv__(self, value: sgt._NumberScalar) -> NPNumber: ...
    def __rfloordiv__(self, value: sgt._NumberScalar) -> NPNumber: ...
    def __ifloordiv__(self, value: sgt._NumberScalar) -> NPNumber: ...
    def __mod__(self, value: sgt._NumberScalar) -> NPNumber: ...
    def __rmod__(self, value: sgt._NumberScalar) -> NPNumber: ...
    def __imod__(self, value: sgt._NumberScalar) -> NPNumber: ...
    def __pow__(self, value: sgt._NumberScalar) -> NPNumber: ...
    def __rpow__(self, value: sgt._NumberScalar) -> NPNumber: ...
    def __ipow__(self, value: sgt._NumberScalar) -> NPNumber: ...
    def __divmod__(self, value: sgt._NumberScalar) -> tuple[NPNumber, NPNumber]: ...
    def __rdivmod__(self, value: sgt._NumberScalar) -> tuple[NPNumber, NPNumber]: ...
    def __abs__(self) -> NPNumber: ...
    @property
    def element_type(
        self,
    ) -> tuple[type[int], type[float], type[complex], type[np.number]]:
        """NPNumberで許可されている型を取得する"""

    @overload
    def count_nonzero(self, axis: None = None, keepdims: bool = False) -> np.intp: ...
    @overload
    def count_nonzero(
        self, axis: np._ShapeLike, keepdims: bool = False
    ) -> NDArray[np.intp]: ...
    def count_nonzero():
        """
        0以外の要素の数を数える

        :param axis: 要素を数える軸を指定する
        :type axis: _ShapeLike | None
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
        q: npt._FloatLike_co,
        axis: sgt.Typeaxis = None,
        method: TYPEMETHOD = "linear",
    ) -> NPNumber:
        """
        指定したパーセンタイルを計算する

        :param q: 求めたいパーセンタイル値を指定する
        :type q: npt._FloatLike_co
        :param axis: 計算する軸の方向を指定する
        :type axis: Typeaxis
        :param method: パーセンタイルを推定するために使用する方法を指定する
        :type method: TYPEMETHOD
        """

    def quantile(
        self,
        q: npt._FloatLike_co,
        axis: sgt.Typeaxis = None,
        method: TYPEMETHOD = "linear",
    ) -> NPNumber:
        """
        指定した分位点を計算する

        :param q: 求めたい分位点を指定する
        :type q: npt._FloatLike_co
        :param axis: 計算する軸の方向を指定する
        :type axis: Typeaxis
        :param method: 分位点を推定するために使用する方法を指定する
        :type method: TYPEMETHOD
        """

    def ratio(self, axis: SupportsIndex | None = None) -> NPNumber:
        """行や列ごとの合計に対する比率を求める"""

    @classmethod
    def zeros(
        cls,
        shape: SupportsIndex,
        dtype: sgt._NumericDTypeLike | None = None,
        order: _OrderCF = "C",
        *,
        device: Literal["cpu"] | None = None,
        like: npt._SupportsArrayFunc | None = None,
    ) -> NPNumber:
        """指定された形状と型の新しい配列を0で埋めた配列を作成する"""

    @classmethod
    def ones(
        cls,
        shape: SupportsIndex,
        dtype: sgt._NumericDTypeLike | None = None,
        order: _OrderCF = "C",
        *,
        device: Literal["cpu"] | None = None,
        like: npt._SupportsArrayFunc | None = None,
    ) -> NPNumber:
        """指定された形状と型の新しい配列を0で埋めた配列を作成する"""

    def zero_check(self) -> NPBool:
        """要素の数値が0の位置を探す"""

    def IQR(
        self,
        axis: sgt.Typeaxis = None,
        method: TYPEMETHOD = "linear",
    ) -> NPNumber:
        """
        配列の四分位数を求める

        :param axis: 計算する軸の方向を指定する
        :type axis: Typeaxis
        :param method: 分位点を推定するために使用する方法を指定する
        :type method: TYPEMETHOD
        """

    def isinf(self) -> NPBool:
        """配列の各要素が正または負の無限大(`np.inf`)かどうかを判定する"""

    def isnan(self) -> NPBool:
        """配列の各要素がNaN(`np.nan`)であるかを判定する"""

    def isfinite(self) -> NPBool:
        """配列の各要素が有限かどうかを判定する"""

    def isposinf(self) -> NPBool:
        """配列の各要素が正の無限大(`+np.inf`)かどうかを判定する"""

    def isreal(self) -> NPBool:
        """配列の各要素が実数かどうかを判定する"""

    def iscomplexobj(self) -> bool:
        """配列の型が複素数型かどうかを判定する"""

    def sorts(
        self,
        axis: SupportsIndex | None = -1,
        kind: _SortKind | None = None,
        order: str | Sequence[str] | None = None,
    ) -> NPNumber:
        """
        配列内の数値を並び替える

        :param axis: ソートの基準となる軸を指定する
        :type axis: SupportsIndex | None
        :param kind: ソートアルゴリズムの種類を指定する
        :type kind: _SortKind | None
        :param order: `NPNumber`がフィールド定義を持つ配列である場合,どのフィールドを優先して比較するかを指定する
        :type order: str | Sequence[str] | None
        """

    @classmethod
    def arange(
        cls,
        start: sgt._NumberScalar,
        /,
        stop: sgt._NumberScalar,
        step: sgt._NumberScalar | None = 1,
        *,
        dtype: sgt._ArangeNumber_DtypeLike,
        device: Literal["cpu"] | None = None,
        like: npt._SupportsArrayFunc | None = None,
    ) -> NPNumber:
        """
        指定された間隔内で等間隔の数値の配列を返す

        :param start: 区間を開始する数値を指定する
        :param stop: 区間を終了する数値を指定する
        :param step: 値の間隔を指定する
        :param dtype: 出力される配列の型を指定する
        :type dtype: dtype
        :param device: 作成された配列を配置する場所を指定する
        :type device: Literal["cpu"] | None
        :param like: NumPy配列ではない配列を作成できるようにする参照するオブジェクトを指定する
        :type like: _SupportsArrayFunc | None
        :return: 指定された間隔内で等間隔の数値の配列を返す
        """

    @classmethod
    def linspace(
        cls,
        start: _ToFloat64,
        stop: _ToFloat64,
        num: SupportsIndex = 50,
        endpoint: bool = True,
        retstep: Literal[False] = False,
        dtype: sgt._RealNumericDTypeLike | None = None,
        axis: SupportsIndex = 0,
        *,
        device: Literal["cpu"] | None = None,
    ) -> NPNumber:
        """
        指定された間隔で等間隔​​の数値の配列を作成する

        :param start: 数列の開始値を指定する
        :param stop:
        シーケンスの終了値を指定する。
        ただし `endpoint`が`False` の場合,生成される値の範囲は[`start`,`stop`)である。
        `endpoint`が`True` の場合,生成される値の範囲は[`start`,`stop`]である。

        :param retstep: `retstep`が`True`の場合,戻り値にステップ数を追加する
        :type retstep: bool
        :param num: 生成する値の数を指定する
        :type num: int
        :param endpoint: 生成させる配列の範囲を指定する
        :type endpoint: bool
        :param dtype: 出力する配列の型を指定する
        :type dtype: dtype
        :param axis: 結果にサンプルを格納する軸を指定する
        :type axis: int
        :param device: 作成された配列を配置するデバイスを指定する
        :type device: Literal["cpu"] | None
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
        ただし `endpoint`が`False` の場合,生成される値の範囲は[`start`,`stop`)である。
        `endpoint`が`True` の場合,生成される値の範囲は[`start`,`stop`]である。

        :param num: 生成する値の数を指定する
        :type num: int
        :param endpoint: 生成させる配列の範囲を指定する
        :type endpoint: bool
        :param base: 対数の底を指定する
        :type base: array_like
        :param dtype: 出力される配列の型を指定する
        :type dtype: dtype
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
        ただし `endpoint`が`False` の場合,生成される値の範囲は[`start`,`stop`)である。
        `endpoint`が`True` の場合,生成される値の範囲は[`start`,`stop`]である。

        :param num: 生成する値の数を指定する
        :type num: int
        :param endpoint: 生成させる配列の範囲を指定する
        :type endpoint: bool
        :param dtype: 出力される配列の型を指定する
        :type dtype: dtype
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
    @classmethod
    def random(
        cls,
        size: sgt._AnyShape | None = None,
        dtype: sgt._DTypeLikeFloat | None = None,
        seed: sgt._Seed = None,
    ) -> NPNumber:
        """
        [0,1)の範囲でランダムな浮動小数点数の配列を作成する

        :param size: 生成する配列の形状を指定する
        :param dtype: 出力される配列の型を指定する
        :param seed: 乱数のシード値を指定する
        """

    @classmethod
    def uniform(
        cls,
        /,
        low: npt._FloatLike_co = 0.0,
        high: npt._FloatLike_co = 1.0,
        size: sgt._AnyShape | None = None,
        dtype: sgt._DTypeLikeFloat | None = None,
        seed: sgt._Seed = None,
    ) -> NPNumber:
        """
        一様分布からなる配列を生成する

        :param low: 生成する乱数の下限値を指定する
        :param high: 生成する乱数の上限値を指定する
        :param shape: 生成する配列の形状を指定する
        :param dtype: 出力される配列の型を指定する
        :param seed: 乱数のシード値を指定する
        """

    @classmethod
    def normal(
        cls,
        /,
        loc: npt._FloatLike_co = 0.0,
        scale: npt._FloatLike_co = 1.0,
        size: sgt._AnyShape | None = None,
        dtype: sgt._DTypeLikeFloat | None = None,
        seed: sgt._Seed = None,
    ) -> NPNumber:
        """
        正規分布からなる配列を生成する

        :param loc: 分布の平均値を指定する
        :param scale: 分布の標準偏差を指定する
        :param shape: 生成する配列の形状を指定する
        :param dtype: 出力される配列の型を指定する
        :param seed: 乱数のシード値を指定する
        """

    @classmethod
    def randint(
        cls,
        /,
        low: int,
        high: int | None = None,
        size: sgt._AnyShape | None = None,
        dtype: sgt._DTypeLikeInt | None = None,
        endpoint: bool = False,
        seed: sgt._Seed = None,
    ) -> NPNumber:
        """
        最小値から最大値までの整数の値からなるランダムに生成された配列を作成する

        :param low: 生成される範囲の最小値を指定する
        :param high: 生成される範囲の最大値を指定する
        :param shape: 生成する配列の形状を指定する
        :param dtype: 出力される配列の型を指定する
        :param endpoint: 生成される区間の範囲を指定する
        :param seed: 乱数のシード値を指定する
        """

    @classmethod
    def logseries(
        cls,
        /,
        p: npt._FloatLike_co,
        size: sgt._AnyShape | None = None,
        dtype: sgt._DTypeLikeFloat | None = None,
        seed: sgt._Seed = None,
    ) -> NPNumber:
        """
        対数級数分布からなる配列を生成する

        :param p: 分布の形状を指定する。`p`の範囲は[0,1)である必要がある。
        :param size: 出力する配列の形状を指定する
        :param dtype: 出力される配列の型を指定する
        :param seed: 乱数のシード値を指定する
        """

HANDLED_FUNCTIONS: dict

def implements(np_function) -> Any:
    """
    numpyの関数を`HANDLED_FUNCTIONS`に登録するデコレータ

    :param np_function: 登録対象のnumpy関数
    :return: デコレータ関数を返す
    """
