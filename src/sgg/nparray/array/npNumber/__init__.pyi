"""基本的な数値の操作をするモジュール"""

from typing import Any, Iterator, Literal, Self, TypeAlias, TypeVar, overload

import numpy as np
from numpy._typing import _ShapeLike
from numpy.typing import DTypeLike, NDArray

from .._typing import _ArrayLikeNumber_co, _NumberT, _ShapeT
from ..npbool import NPBool

_DTypeT = TypeVar(
    "_DTypeT", bound=np.dtype, default=np.dtype[np.float64], covariant=True
)
__all__ = ["NPNumber"]
TYPEMETHOD: TypeAlias = Literal[
    "averaged_inverted_cdf",
    "closest_observation",
    "hazen",
    "interpolated_inverted_cdf",
    "inverted_cdf",
    "linear",
    "median_unbiased",
    "normal_unbiased",
    "weibull",
]
HANDLED_FUNCTIONS: dict

def implements(np_function) -> Any:
    """
    numpyの関数を`HANDLED_FUNCTIONS`に登録するデコレータ

    :param np_function: 登録対象のnumpy関数
    :return: デコレータ関数を返す
    """

class NPNumber(np.ndarray[_ShapeT, np.dtype[_DTypeT]]):
    """`np.ndarray`を継承した数値型の配列クラス"""

    @overload
    def __new__(
        cls,
        data: _ArrayLikeNumber_co,
        dtype: None = np.float64,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
    ) -> NPNumber[_ShapeT, np.dtype[np.float64]]: ...
    @overload
    def __new__(
        cls,
        data: _ArrayLikeNumber_co,
        dtype: type[_NumberT],
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
    ) -> NPNumber[_ShapeT, np.dtype[_NumberT]]: ...
    @overload
    def __new__(
        cls,
        data: _ArrayLikeNumber_co,
        dtype: type[_NumberT] | None = np.float64,
        d_ndim: int | None = None,
        min_ndim: int | None = None,
        max_ndim: int | None = None,
    ) -> Self:
        """
        新しい配列オブジェクトインスタンスを生成する

        :param data: 変換する配列を指定する
        :type data: _ArrayLikeNumber_co
        :param dtype: 配列の型を指定する
        :type dtype: type[_NumberT] | None
        :param d_ndim: 固定される次元数を指定する
        :type d_ndim: int | None
        :param min_ndim: 許容する最小次元数を指定する
        :type min_ndim: int | None
        :param max_ndim: 許容する最大次元数を指定する
        :type max_ndim: int | None
        :return: 生成された配列オブジェクトインスタンスを返す
        :rtype: Self
        :raises ValueError: 次元数が範囲外の場合に発生させる
        :raises TypeError: 要素型が`__element_type`と一致しない場合に発生させる
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
        min_ndim: int | None,
        max_ndim: int | None,
    ) -> None:
        """
        配列の次元数がmin_ndim・max_ndimの範囲内か検証する

        :param obj: 検証対象の配列
        :param min_ndim: 許可する最小次元数を指定する。Noneの場合は制約なし
        :param max_ndim: 許可する最大次元数を指定する。Noneの場合は制約なし
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
        """スライスやview後もdtypeや次元数情報を引き継がさせるメソッド"""

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

    def __eq__(self, other: Any) -> NPBool[Any, np.dtype[np.bool_]]: ...
    def __ne__(self, other: Any) -> NPBool[Any, np.dtype[np.bool_]]: ...
    def __lt__(self, other: Any) -> NPBool[Any, np.dtype[np.bool_]]: ...
    def __le__(self, other: Any) -> NPBool[Any, np.dtype[np.bool_]]: ...
    def __gt__(self, other: Any) -> NPBool[Any, np.dtype[np.bool_]]: ...
    def __ge__(self, other: Any) -> NPBool[Any, np.dtype[np.bool_]]: ...
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

    @property
    def element_type(
        self,
    ) -> tuple[tuple[int], tuple[float], tuple[complex], tuple[np.number]]:
        """NPNumberで許可されている型を取得する"""

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
    def dtypes(self, dtype: DTypeLike | None) -> np.dtype | None:
        """
        配列のdtypeを設定する

        :param dtype: 配列の型を指定する
        :type dtype: DTypeLike | None
        :return:
        :rtype: numpy.dtype | None
        """

    @property
    def min_ndim(self) -> int | None:
        """配列オブジェクトが許容する最小次元数を返す"""

    @property
    def max_ndim(self) -> int | None:
        """配列オブジェクトが許容する最大次元数を返す"""

    def to_1d(self) -> NPNumber:
        """
        配列を1次元にフラット化した新しい配列オブジェクトを返す

        :return: フラット化した配列オブジェクトを返す
        :raises ValueError: `min_ndim`が1以下の場合に発生させる
        """

    def lengtharange(self) -> NDArray[np.unsignedinteger[np._64Bit]]:
        """
        配列オブジェクトと同じ`shape`を持つ,各軸の最終次元インデックスの配列を返す

        `dtype`は`np.uint64`に固定される

        :return: インデックス配列を返す
        """

    def shapesize(self, shapes: tuple[int, ...]) -> bool:
        """
        配列オブジェクトの`shape`が`shapes`と一致するかを確認する

        :param shapes: 比較する`shape`を指定する
        :type shapes: tuple[int, ...]
        :return: `shape`が一致する場合は`True`を返し,一致しない場合は`False`を返す
        :rtype: bool
        """

    def roll(self, shift: _ShapeLike, axis: _ShapeLike | None = None) -> NPNumber:
        """
        要素を指定された軸に沿って回転させる

        :param shift: 要素を移動させる位置の数を指定する
        :type shift: _ShapeLike
        :param axis: 要素を移動させる軸を指定する
        :type axis: _ShapeLike | None
        """

    def rot90(self, k: int = 1, axes: tuple[int, int] = (0, 1)) -> NPNumber:
        """
        指定された軸の平面内で配列を90度回転させる

        :param k: 配列に90度回転させたい回数を指定する
        :type k: int
        :param axes: 平面内で回転される軸を指定する
        :type axes: tuple[int,int]
        :return: 回転させた配列を返す
        :rtype: NPNumber
        """

    def tonumpy(self) -> NDArray[Any]:
        """配列オブジェクトオブジェクトを`np.ndarray`オブジェクトに変換する"""

    def typeconversion(
        self,
        type: np.DTypeLike,
        casting: Literal[
            "no", "equiv", "safe", "same_kind", "same_value", "unsafe"
        ] = "safe",
    ) -> bool:
        """
        配列の型が`type`で指定された型に変換可能か調べる

        :param type: 型変換先のデータ型を指定する
        :type type: np.DTypeLike
        :param casting: どのようなデータ変換が行われるか指定する
        :type casting: Literal["no", "equiv", "safe", "same_kind", "same_value", "unsafe"]
        """

    def all_None(self) -> bool:
        """
        配列内の全要素が`None`かどうかを返す

        :return: 配列内の全要素が`None`の場合は`True`を返し,そうでなければ`False`を返す
        :rtype: bool
        """

    def any_None(self) -> bool:
        """
        配列内のいずれかの要素が`None`かどうかを返す

        :return: `None`の要素が1つでもある場合は`True`を返し,そうでなければ`False`を返す
        :rtype: bool
        """

    def count_nonzero(
        self, axis: np._ShapeLike | None = None, keepdims: bool = False
    ) -> np.intp | NDArray[np.intp]:
        """
        0以外の要素の数を数える

        :param axis: 要素を数える軸を指定する
        :type axis: _ShapeLike | None
        :param keepdims: 要素の数を数えた戻り値をサイズ1の次元にするか指定する。
        :type keepdims: bool
        """

    def unique(self) -> NDArray:
        """配列の固有要素を見つける"""

    def counts(self) -> tuple[NDArray[Any], NDArray[np.intp]]:
        """配列内の要素とその要素が配列内に存在する個数を返す"""

    @property
    def sturgesval(self) -> np.floating:
        """スタージェスの公式を求める"""

    def cussum(self) -> NPNumber[_ShapeT, _DTypeT]:
        """一つ前の元の値との和を求める"""

    def cumprod(self) -> NPNumber[_ShapeT, _DTypeT]:
        """一つ前の元の値との積を求める"""

    def percentile(
        self,
        q: tuple[int | float, ...],
        method: TYPEMETHOD = "linear",
    ) -> NPNumber:
        """
        指定したパーセンタイルを計算する

        :param q: 求めたいパーセンタイル値を指定する
        :type q: tuple[int | float,...]
        :param method: パーセンタイルを推定するために使用する方法を指定する
        :type method: Literal["inverted_cdf","averaged_inverted_cdf","closest_observation","interpolated_inverted_cdf","hazen","weibull","linear","median_unbiased","normal_unbiased"]
        """

    def quantile(
        self,
        q: tuple[float, ...],
        method: TYPEMETHOD = "linear",
    ) -> NPNumber:
        """
        指定した分位点を計算する

        :param q: 求めたい分位点を指定する
        :type q: tuple[float,...]
        :param method: 分位点を推定するために使用する方法を指定する
        :type method: Literal["inverted_cdf","averaged_inverted_cdf","closest_observation","interpolated_inverted_cdf","hazen","weibull","linear","median_unbiased","normal_unbiased"]
        """

    def ratio(self, axis: int | None = None) -> NPNumber:
        """行や列ごとの合計に対する比率を求める"""

    def zero_check(self) -> NPBool[Any, np.dtype[np.bool_]]:
        """要素の数値が0の位置を探す"""
