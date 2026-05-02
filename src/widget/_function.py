from ..types import Any
from ._color import Color
from .developer import LIST,Number
__all__=['bols','Color','ints','intsmin','listchose','nums','numsmin','parsecolor','typelist','int0','int0s','int1s','list2float','list2int','list2num','list4float','list4int','list4num','num0','num0s','num1s','range_num']
def list2num(lin:list[Any]|tuple[Any]=None)->bool:return True if isinstance(lin,(list,tuple)) and len(lin)==2 and all(isinstance(i,(int,float,Number))for i in lin) else False
def list2int(lin:list[Any]|tuple[Any]=None)->bool:return True if isinstance(lin,(list,tuple)) and len(lin)==2 and all(isinstance(i,int)for i in lin) else False
def list2float(lin:list[Any]|tuple[Any]=None)->bool:return True if isinstance(lin,(list,tuple)) and len(lin)==2 and all(isinstance(i,float)for i in lin) else False
def list4num(lin:list[Any]|tuple[Any]=None)->bool:return True if isinstance(lin,(list,tuple)) and len(lin)==4 and all(isinstance(i,(int,float,Number))for i in lin) else False
def list4int(lin:list[Any]|tuple[Any]=None)->bool:return True if isinstance(lin,(list,tuple)) and len(lin)==4 and all(isinstance(i,int)for i in lin) else False
def list4float(lin:list[Any]|tuple[Any]=None)->bool:return True if isinstance(lin,(list,tuple)) and len(lin)==4 and all(isinstance(i,float)for i in lin) else False
def typelist(val:Any)->bool:
 '''`val`が配列かを調べる'''
 if isinstance(val,(LIST,tuple,list)):return True
 return False
def listchose(val:str,arr:list,other:str|None=None)->str:
 '''`val`が`arr`の配列内の要素に存在するかを調べる。存在しなかった場合,`other`を返す。もし`other`がNoneの場合で尚且つarrが配列の場合,arrの最初の要素を返す。

 :param val: 検索したい値を指定する。
 :type val: str
 :param arr: 検索するデータを指定する。
 :type arr: list
 :param other: `val`が`arr`に存在しなかった場合に返す値を指定する。
 :type other: str|None
 :return: 配列の要素を返す。
 :rtype: str'''
 if isinstance(arr,(tuple,list))and other==None:other=arr[0]
 elif not isinstance(arr,(tuple,list))and other==None:other=arr
 if val in arr:return val
 return other
def numsmin(val:int|float|Number,mins:int|float|Number=0,other:Any=None)->int|float|Number|Any:
 if not isinstance(val,(int,float,Number)) or not isinstance(mins,(int,float,Number)):
  return other
 if isinstance(val,Number):val=val.val
 if isinstance(mins,Number):mins=mins.val
 if mins<val:return val
 return other
def nums(val:int|float,other:int|float|Number|None=None)->int|float|Number|None:
 '''`val`が数値かを調べる。

 :param val: 調べたい値もしくはデータを指定する。
 :type val: int|float
 :param other: 調べたい値`val`がint|float型ではなかったときに返す値を指定する。
 :type other: int|float|Number|None
 :return: 数値を返す。
 :rtype: int|float|Number|None'''
 return val if isinstance(val,(int,float)) else other
def num1s(val:int|float|Number=0,mins:int|float|Number=1)->int|float|Number:
 '''`val`が1以上の数値かを調べる。

 :param val: 調べたい数値を指定する。
 :type val: int|float
 :param mins: 調べたい数値`val`の最低値を指定する。
 :type mins: int|float|Number|None
 :return: 数値を返す。
 :rtype: int|float|Number|None'''
 return val if isinstance(val,(int,float,Number))and 1<=val else mins
def num0s(val:int|float|Number=0,mins:int|float|Number=0)->int|float|Number:
 '''`val`が0以上の数値かを調べる。

 :param val: 調べたい数値を指定する。
 :type val: int|float|Number
 :param mins: 調べたい数値`val`の最低値を指定する。
 :type mins: int|float|Number
 :return: 数値を返す。
 :rtype: int|float|Number'''
 return val if isinstance(val,(int,float,Number))and 0<=val else mins
def num0(val:int|float|Number=0,mins:int|float|Number=0)->int|float|Number:
 '''`val`が0より大きい数値かを調べる。

 :param val: 調べたい数値を指定する。
 :type val: int|float
 :param mins: 調べたい数値`val`の最低値を指定する。
 :type mins: int|float
 :return: 数値を返す。
 :rtype: int|float'''
 return val if isinstance(val,(int,float,Number))and 0<val else mins
def intsmin(val:int,mins:int=0,other:Any=None)->int:
 if not isinstance(val,int) or not isinstance(mins,int):
  return other
 if mins<val:return val
 return other
def ints(val:int=0,other:int=None)->int:
 '''`val`がint型かを調べる。

 :param val: 調べたい数値を指定する。
 :type val: int
 :param other: 調べたい値`val`がint型ではなかったときに返す値を指定する。
 :type other: int
 :return: 数値を返す。
 :rtype: int'''
 return val if isinstance(val,int) else other
def int1s(val:int=0,mins:int=1)->int:
 '''`val`が1以上の正の整数かを調べる。

 :param val: 調べたい数値を指定する。
 :type val: int
 :param mins: 調べたい数値`val`の最低値を指定する。
 :type mins: int
 :return: 数値を返す。
 :rtype: int'''
 return val if isinstance(val,int)and 1<=val else mins
def int0s(val:int=0,mins:int=0)->int:
 '''`val`が0以上の正の整数かを調べる。

 :param val: 調べたい数値を指定する。
 :type val: int
 :param mins: 調べたい数値`val`の最低値を指定する。
 :type mins: int
 :return: 数値を返す。
 :rtype: int'''
 return val if isinstance(val,int)and 0<=val else mins
def int0(val:int=0,mins:int=0)->int:
 '''`val`が0より大きいの正の整数かを調べる。

 :param val: 調べたい数値を指定する。
 :type val: int
 :param mins: 調べたい数値`val`の最低値を指定する。
 :type mins: int
 :return: 数値を返す。
 :rtype: int'''
 return val if isinstance(val,int)and 0<val else mins
def range_num(
val:int|float,
mins:int|float=None,
maxs:int|float=None,
others:int|float=None
)->int|float:
 '''`val`が`mins`から`maxs`の範囲内化を調べる。

 :param val: 範囲内かを調べたい数値を指定する。
 :type val: int|float
 :param mins: 範囲の最低値を指定する。
 :type mins: int|float
 :param maxs: 範囲の最大値を指定する。
 :type maxs: int|float
 :param others: 指定した`val`が指定した範囲ではなかった場合に返す値を指定する。
 :type others: int|float
 :return: 数値を返す。
 :rtype: int|float'''
 if (not isinstance(mins,(int,float))) or (not isinstance(maxs,(int,float))):return others
 if maxs<mins:mins,maxs=maxs,mins
 if mins<=val<=maxs:return val
 return others
def bols(j:bool,o:bool=True)->bool:
 '''`j`がbool型かを判断する。

 :param j: bool型か調べたい値を指定する。
 :type j: bool
 :param other: `j`がbool型ではなかったときに返す値を指定する。
 :type other: bool
 :return: bool型を返す。
 :rtype: bool'''
 if isinstance(j,bool):return j
 return o
def parsecolor(val:str,other:str=None)->str:
 '''`Color`を文字列で返す。

 :param value: 色名を指定する。
 :type value: str
 :param other: `value`がNoneなどの色の値ではない時に指定する色を指定する。
 :type other: str
 :return: 色名を返す。
 :rtype: str'''
 return str(Color(val,other))