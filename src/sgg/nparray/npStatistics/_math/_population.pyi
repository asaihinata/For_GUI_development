'''母集団についての計算をする。'''
from numpy import float64,ndarray
__all__=['cCoefficient','Population']
def cCoefficient(p:float=0.95)->float64:'''信頼係数を求める

 :param p: 信頼係数の割合を指定する。
 :type p: float
 :raises TypeError: `p`がfloat型を指定しなかった場合に発生させる
 :raises ValueError: `p`が0.0から1.0の範囲外を指定した場合に発生させる'''
class Population:
 data:ndarray
 def __init__(self,data:ndarray)->None:...
 @property
 def n(self)->int:...
 @property
 def ave(self):'''母平均を求める'''
 @property
 def var(self):'''母分散を求める'''
 @property
 def SD(self):'''母標準偏差を求める'''
 def ratio_E_samplingerror(self,p:float):'''母比率の標本誤差を求める

 :param p: 割合を0.0から1.0の範囲の浮動小数点数で指定する。
 :type p: float
 :raises TypeError: `p`をfloat型で指定しなかった場合に発生させる
 :raises ValueError: 0.0<=`p`<=1.0の範囲で指定しなかった場合に発生させる'''
 def ratio_E(self,p:float):'''母比率の上限値と下限値を求める

 :param p: 割合を0.0から1.0の範囲の浮動小数点数で指定する。
 :type p: float
 :raises TypeError: `p`をfloat型で指定しなかった場合に発生させる
 :raises ValueError: 0.0<=`p`<=1.0の範囲で指定しなかった場合に発生させる'''
 def ratio_E_range(self,p:float):'''母比率の信頼区画を求める

 :param p: 割合を0.0から1.0の範囲の浮動小数点数で指定する。
 :type p: float
 :raises TypeError: `p`をfloat型で指定しなかった場合に発生させる
 :raises ValueError: 0.0<=`p`<=1.0の範囲で指定しなかった場合に発生させる'''
 def ratio_E_max(self,p:float):'''母比率の上限値を求める

 :param p: 割合を0.0から1.0の範囲の浮動小数点数で指定する。
 :type p: float
 :raises TypeError: `p`をfloat型で指定しなかった場合に発生させる
 :raises ValueError: 0.0<=`p`<=1.0の範囲で指定しなかった場合に発生させる'''
 def ratio_E_min(self,p:float):'''母比率の下限値を求める

 :param p: 割合を0.0から1.0の範囲の浮動小数点数で指定する。
 :type p: float
 :raises TypeError: `p`をfloat型で指定しなかった場合に発生させる
 :raises ValueError: 0.0<=`p`<=1.0の範囲で指定しなかった場合に発生させる'''
 def ave_E_samplingerror(self,p:float=0.95):'''母平均の標本誤差を求める'''
 def ave_E(self,p:float=0.95):'''母平均の上限値と下限値を求める'''
 def ave_E_range(self,p:float=0.95):'''母平均の範囲を求める'''
 def ave_E_max(self,p:float=0.95):'''母平均の上限値を求める'''
 def ave_E_min(self,p:float=0.95):'''母平均の下限値を求める'''