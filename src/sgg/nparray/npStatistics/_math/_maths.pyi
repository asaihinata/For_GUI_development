import numpy as np
from numpy._typing import _ArrayLikeFloat_co
from numpy.typing import NDArray
__all__=['mdeviation','mdevsq','moutlier','mregression','mone_regression','mFregression']
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