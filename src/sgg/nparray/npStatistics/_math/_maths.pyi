from typing import Any
import numpy as np
from numpy._typing import _ArrayLikeFloat_co
from numpy.typing import ArrayLike,NDArray
__all__=['mdeviation','mdevsq','moutlier','mFregression','mregression','mone_regression','fisher_ztransformation','fzt_test_statistic','Euclidean_distance']
def mdeviation(data):'''偏差値を求める'''
def mdevsq(data):'''偏差平方和を求める'''
def moutlier(data):'''外れ値を求める'''
def mFregression(
x:np.ndarray,
y:np.ndarray,
Fx:_ArrayLikeFloat_co,
n:int=1
)->NDArray[np.floating]:'''点`Fx`において点(x,y)に次数`n`の多項式を評価する。

 :param Fx: 評価したい点を指定する。
 :type Fx: _ArrayLikeFloat_co
 :param n: 次数を指定する。
 :type n: int'''
def mregression(
x:np.ndarray,
y:np.ndarray,
n:int=1
)->NDArray[np.floating]:'''点(x,y)の回帰直線を求める。'''
def mone_regression(
x:np.ndarray,
y:np.ndarray
)->NDArray[np.floating]:'''点(x,y)に一次方程式の回帰直線を返す。

 :return: [傾き,切片]として返す。
 :rtype: NDArray[floating]'''
def fisher_ztransformation(r:int|float):'''フィッシャーのz変換を求める。

 :param r: 標本相関係数を指定する。
 :type r: int|float'''
def fzt_test_statistic(r:int|float,r0:int|float,n:int):
 '''フィッシャーのz変換を用いた母相関係数の検定統計量Zを求める。

 :param r: 標本相関係数を指定する。
 :type r: int|float
 :param r0: 基準値を指定する。
 :type r0: int|float
 :param n: データの数を指定する。
 :type n: int'''
def Euclidean_distance(
a:ArrayLike,
b:ArrayLike
)->np.floating[Any]:'''ユーグリットの距離を使い点`a`と点`b`の距離を求める。

 :param a: 点aを指定する。
 :type a: ArrayLike
 :param b: 点bを指定する。
 :type b: ArrayLike
 :return: 点`a`と点`b`の距離を返す。
 :rtype: np.floating[Any]'''