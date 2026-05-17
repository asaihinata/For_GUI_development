import numpy as np
from ....typing import *
__all__=['sturges']
@overload
def sturges(
n:list|tuple|np.ndarray|int,
type:Literal['ceil','floor','round']=...
)->int:'''ヒストグラムの階級数を求めるときに使用する(スタージェスの公式)。

 :param n: データの件数もしくはデータを指定する。
 :type n: list|tuple|np.ndarray|int
 :param type: 小数の処理を指定する。
 :type type: Literal['ceil','floor','round']
 :raises TypeError: `n`に整数型もしくは配列の型を指定しなかった場合に発生させる
 :return: 計算結果を返す。
 :rtype: int'''
@overload
def sturges(
n:list|tuple|np.ndarray|int,
type:Literal['ceil','floor','round']='ceil'
)->int:'''ヒストグラムの階級数を求めるときに使用する(スタージェスの公式)。
小数点以下を切り上げて計算する。

 :param n: データの件数もしくはデータを指定する。
 :type n: list|tuple|np.ndarray|int
 :param type: 小数の処理を指定する。
 :type type: Literal['ceil','floor','round']
 :raises TypeError: `n`に整数型もしくは配列の型を指定しなかった場合に発生させる
 :return: 計算結果を返す。
 :rtype: int'''
@overload
def sturges(
n:list|tuple|np.ndarray|int,
type:Literal['ceil','floor','round']='floor'
)->int:'''ヒストグラムの階級数を求めるときに使用する(スタージェスの公式)。
小数点以下を切り捨てて計算する。

 :param n: データの件数もしくはデータを指定する。
 :type n: list|tuple|np.ndarray|int
 :param type: 小数の処理を指定する。
 :type type: Literal['ceil','floor','round']
 :raises TypeError: `n`に整数型もしくは配列の型を指定しなかった場合に発生させる
 :return: 計算結果を返す。
 :rtype: int'''
@overload
def sturges(
n:list|tuple|np.ndarray|int,
type:Literal['ceil','floor','round']='round'
)->int:'''ヒストグラムの階級数を求めるときに使用する(スタージェスの公式)。
小数点以下を四捨五入して計算する。

 :param n: データの件数もしくはデータを指定する。
 :type n: list|tuple|np.ndarray|int
 :param type: 小数の処理を指定する。
 :type type: Literal['ceil','floor','round']
 :raises TypeError: `n`に整数型もしくは配列の型を指定しなかった場合に発生させる
 :return: 計算結果を返す。
 :rtype: int'''