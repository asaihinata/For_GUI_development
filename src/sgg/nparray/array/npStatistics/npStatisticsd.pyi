"""基本的な統計の計算をするモジュール"""

from typing import (Any, Generator, Literal, Self, SupportsIndex, TypeAlias,
                    TypeVar, overload)

import numpy as np
from numpy.typing import ArrayLike, DTypeLike, NDArray

from sgg.typing import TypeArrayLikeNumber, _ArrayLikeNumber_co, _NumberT

from ..dev import NDArrayOperatorsMixin, _ArrayCommonMixin

__all__ = ["NPStatisticsd"]
_ShapeT = TypeVar("_ShapeT", bound=tuple[int], default=tuple[int], covariant=True)
_DTypeT = TypeVar(
    "_DTypeT", bound=np.dtype, default=np.dtype[np.float64], covariant=True
)

Type_Method: TypeAlias = Literal[
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
BINS_LIST: TypeAlias = Literal[
    "stone", "auto", "scott", "doane", "fd", "rice", "sqrt", "sturges"
]
HANDLED_FUNCTIONS: dict

def implements(np_function) -> Any:
    """
    numpyの関数を`HANDLED_FUNCTIONS`に登録するデコレータ

    :param np_function: 登録対象のnumpy関数
    :return: デコレータ関数を返す
    """

class NPStatisticsd(_ArrayCommonMixin, NDArrayOperatorsMixin, np.ndarray):
    """`np.ndarray`を継承した基本的な統計を計算する配列クラス"""

    def __new__(
        cls,
        data: _ArrayLikeNumber_co,
        dtype: _NumberT | None = np.float64,
    ) -> Self:
        """
        基本的な統計の計算をする

        :param data: 数値が入った一次元の配列を指定する
        :type data: _ArrayLikeNumber_co
        :param dtype: `NPStatisticsd`内の配列の型を指定する
        :type dtype: _NumberT | None
        :rtype: Self
        :return: `NPStatisticsd`オブジェクトを返す
        """

    @classmethod
    def _resolve_dtype(
        cls,
        dtype: np.dtype | str | type | None,
    ) -> np.dtype | None:
        """
        引数dtypeを解決させる

        :param dtype: ユーザーが指定するdtype
        :return: 解決されたdtypeを返す
        :rtype: numpy.dtype | None
        """

    @classmethod
    def _validate_ndim(
        cls,
        obj: np.ndarray,
    ) -> None:
        """
        配列の次元数が1次元か検証する

        :param obj: 検証対象の配列
        :raises ValueError: 次元数が範囲外の場合に発生させる
        """

    @classmethod
    def _validate_elements(cls, obj: np.ndarray) -> None:
        """
        配列内の要素が`__element_type`と一致するか検証する

        :param obj: 検証対象の配列
        :raises TypeError: 許可されていない型の要素が含まれる場合に発生させる
        """

    def __array_finalize__(self, obj: np.ndarray | None) -> None:
        """スライスやview後もdtype情報を引き継がさせるメソッド"""

    def __array_ufunc__(
        self,
        ufunc: np.ufunc,
        method: str,
        *inputs: Any,
        **kwargs: Any,
    ) -> NPStatisticsd | Any:
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

    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def __contains__(self, value: object) -> bool: ...
    def __iter__(self) -> Generator[tuple[NDArray[Any], ...], Any, None]: ...
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

    @property
    def element_type(
        self,
    ) -> tuple[tuple[int], tuple[float], tuple[complex], tuple[np.number]]:
        """NPStatisticsdで許可されている型を取得する"""

    @property
    def data(self) -> NDArray[Any]:
        """配列オブジェクトオブジェクトを`np.ndarray`オブジェクトに変換する"""

    @property
    def dtypes(self) -> np.dtype | None:
        """
        インスタンス生成時に確定したdtypeを取得する

        :return:
        :rtype: numpy.dtype | None
        """

    @dtypes.setter
    def dtypes(self, dtype: DTypeLike | None) -> None:
        """
        配列のdtypeを設定する

        :param dtype: 配列の型を指定する
        :type dtype: DTypeLike | None
        """

    @property
    def sum(self) -> np.number:
        """配列の全要素の合計を求める"""

    @property
    def mean(self) -> np.floating:
        """配列の算術平均を求める"""

    @property
    def ave(self) -> np.floating:
        """配列の加重平均を求める"""

    @property
    def max(self) -> np.number:
        """配列の最大値を求める"""

    @property
    def min(self) -> np.number:
        """配列の最小値を求める"""

    @property
    def var(self) -> np.floating:
        """配列の分散を求める"""

    @property
    def std(self) -> np.floating:
        """配列の標準偏差を求める"""

    @property
    def pow2(self) -> TypeArrayLikeNumber:
        """配列の各要素を2乗した値を求める"""

    @property
    def deviation(self) -> TypeArrayLikeNumber:
        """配列内の各要素の偏差値を求める"""

    @property
    def log(self) -> TypeArrayLikeNumber:
        """配列の各要素の底が`e`の対数を求める"""

    @property
    def log10(self) -> TypeArrayLikeNumber:
        """配列の各要素の底が`10`の対数を求める"""

    @property
    def log2(self) -> TypeArrayLikeNumber:
        """
        配列の各要素の底が`2`の対数を求める

        ``numpy.log2`` を使用して計算する
        """

    @property
    def log1p(self) -> TypeArrayLikeNumber:
        """配列の各要素について`log(1+x)`を求める"""

    @property
    def devsq(self) -> np.floating:
        """偏差平方和を求める"""

    @property
    def range(self) -> NDArray[Any]:
        """
        配列の最小値と最大値を求める

        :return: `[最小値,最大値]`の形式の配列を返す
        :rtype: NDArray[Any]
        """

    @property
    def skew(self) -> np.floating:
        """歪度を求める"""

    @property
    def kurtosis(self) -> np.floating:
        """尖度を求める"""

    @property
    def n(self) -> int:
        """配列の長さの数を返す"""

    @property
    def n1(self) -> int:
        """配列の長さの数-1の値を返す"""

    @property
    def CV(self) -> np.floating:
        """変動係数を求める"""

    def percentile(
        self,
        q: tuple[int | float, ...],
        method: Type_Method = "linear",
    ) -> np.floating | NDArray[np.floating]:
        """
        指定したパーセンタイルを計算する

        :param q: 求めたいパーセンタイル値を指定する
        :type q: tuple[int | float,...]
        :param method: パーセンタイルを推定するために使用する方法を指定する
        :type method: Type_Method
        """

    def quantile(
        self,
        q: tuple[float, ...],
        method: Type_Method = "linear",
    ) -> np.floating | NDArray[np.floating]:
        """
        指定した分位点を計算する

        :param q: 求めたい分位点を指定する
        :type q: tuple[float,...]
        :param method: 分位点を推定するために使用する方法を指定する
        :type method: Type_Method
        """

    def IQR(
        self,
        method: Type_Method = "linear",
    ) -> NDArray[np.floating]:
        """
        配列の四分位範囲を求める

        :param method: 分位点を推定するために使用する方法を指定する
        :type method: Type_Method
        """

    @property
    def outlier(self) -> NDArray[np.floating]:
        """四分位範囲の外れ値を求める"""

    def hist_bin_edges(
        self,
        bin: int | BINS_LIST | ArrayLike = 10,
        range: tuple[float, float] | None = None,
        weights: ArrayLike | None = None,
    ) -> NDArray[Any]:
        """
        `bin`で指定された計算方法で計算されたビンの境界を求める

        :param bin: ビンの数や計算方法を指定する
        :type bin: int | BINS_LIST | ArrayLike
        :param range: ビンの下限と上限を指定する
        :type range: tuple[float,float] | None
        :param weights: 重みを指定する
        :type weights: ArrayLike | None
        :return: `bin`で指定された計算方法で計算した結果を返す
        :rtype: NDArray[Any]
        """

    def histogram(
        self,
        bin: int | BINS_LIST | ArrayLike = 10,
        range: tuple[float, float] | None = None,
        weights: ArrayLike | None = None,
    ) -> tuple[NDArray, NDArray]:
        """
        配列のヒストグラムを求める

        :param bin: ビンの数や計算方法を指定する
        :type bin: int | BINS_LIST | ArrayLike
        :param range: ビンの下限と上限を指定する
        :type range: tuple[float,float] | None
        :param weights: 重みを指定する
        :type weights: ArrayLike | None
        :return: 区間内のデータの個数と区間を区切る境界の値を返す
        :rtype: tuple[NDArray,NDArray]
        """

    def bincount(
        self, weights: ArrayLike | None = None, min: SupportsIndex = 0
    ) -> NDArray[np.intp]:
        """
        非負整数の配列に含まれる各値の出現回数を数える

        :param weights: 重みを指定する
        :type weights: ArrayLike | None
        :param min: 出力配列の最小ビン数を指定する
        :type min: SupportsIndex
        :return: 入力配列をビン分割した結果を返す
        :rtype: NDArray[np.intp]
        """

    def ratio_E_samplingerror(
        self, parcent: int | float, cc: int | float
    ) -> np.float64:
        """
        母比率の標本誤差を求める

        :param parcent: 割合を指定する
        :type parcent: int | float
        :param cc: 信頼係数を指定する
        :type cc: int | float
        :raises TypeError: `parcent`をint型もしくはfloat型で指定しなかった場合に発生させる
        :raises ValueError: 0.0<=`parcent`<=1.0の範囲で指定しなかった場合に発生させる
        :raises TypeError: 信頼係数`cc`にint型もしくはfloat型で指定しなかった場合に発生させる
        :raises ValueError: 信頼係数`cc`に0.0から1.0の範囲で指定しなかった場合に発生させる
        """

    def ratio_E(self, p: int | float) -> tuple[np.float64, np.float64]:
        """
        母比率の上限値と下限値を求める

        :param parcent: 割合を指定する
        :type parcent: int | float
        :param cc: 信頼係数を指定する
        :type cc: int | float
        :raises TypeError: `parcent`をint型もしくはfloat型で指定しなかった場合に発生させる
        :raises ValueError: 0.0<=`parcent`<=1.0の範囲で指定しなかった場合に発生させる
        :raises TypeError: 信頼係数`cc`にint型もしくはfloat型で指定しなかった場合に発生させる
        :raises ValueError: 信頼係数`cc`に0.0から1.0の範囲で指定しなかった場合に発生させる
        """

    def ave_E_samplingerror(self, cc: int | float = 0.95) -> np.float64:
        """
        母平均の推定をする

        :param cc: 信頼係数を指定する
        :type cc: int | float"""

    def ave_E(self, cc: float = 0.95) -> tuple[np.float64, np.float64]:
        """
        母平均の上限値と下限値を求める

        :param cc: 信頼係数を指定する
        :type cc: int | float
        """

def cCoefficient(p: int | float = 0.95) -> np.float64:
    """
    信頼係数を求める

    :param p: 信頼係数を指定する
    :type p: int | float
    :raises TypeError: `p`がfloat型を指定しなかった場合に発生させる
    :raises ValueError: `p`が0.0から1.0の範囲外を指定した場合に発生させる
    """
