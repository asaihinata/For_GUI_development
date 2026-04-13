from ..types import Any,Numbertype
from ._color import Color
from .developer import LIST
__all__=['bols','ints','listchose','nums','parsecolor','typelist','int0','int0s','int1s','list2float','list2int','list2num','list4float','list4int','list4num','num0','num0s','num1s','range_num']
def list2num(lin:list|tuple=None)->bool:return True if isinstance(lin,(list,tuple)) and len(lin)==2 and all(isinstance(i,(int,float))for i in lin) else False
def list2int(lin:list|tuple=None)->bool:return True if isinstance(lin,(list,tuple)) and len(lin)==2 and all(isinstance(i,int)for i in lin) else False
def list2float(lin:list|tuple=None)->bool:return True if isinstance(lin,(list,tuple)) and len(lin)==2 and all(isinstance(i,float)for i in lin) else False
def list4num(lin:list|tuple=None)->bool:return True if isinstance(lin,(list,tuple)) and len(lin)==4 and all(isinstance(i,(int,float))for i in lin) else False
def list4int(lin:list|tuple=None)->bool:return True if isinstance(lin,(list,tuple)) and len(lin)==4 and all(isinstance(i,int)for i in lin) else False
def list4float(lin:list|tuple=None)->bool:return True if isinstance(lin,(list,tuple)) and len(lin)==4 and all(isinstance(i,float)for i in lin) else False
def typelist(val:Any)->bool:
 '''val`が配列かを調べる'''
 if isinstance(val,(LIST,tuple,list)):return True
 return False
def listchose(val:str,arr:list,other:str|None=None)->str:
 '''`val`が`arr`の配列内の要素に存在するかを調べる。存在しなかった場合,otherを返す。もしotherがNoneの場合で尚且つarrが配列の場合,arrの最初の要素を返す。

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
def nums(val:Numbertype,other:Numbertype=None)->Numbertype:
 '''`val`が数値かを調べる。

 :param val: 調べたい値もしくはデータを指定する。
 :type val: Numbertype
 :param other: 調べたい値`val`がNumbertype型ではなかったときに返す値を指定する。
 :type other: Numbertype
 :return: 数値を返す。
 :rtype: Numbertype'''
 return val if isinstance(val,(int,float)) else other
def num1s(val:Numbertype=0,mins:Numbertype=1)->Numbertype:
 '''`val`が1以上の数値かを調べる。

 :param val: 調べたい数値を指定する。
 :type val: Numbertype
 :param mins: 調べたい数値`val`の最低値を指定する。
 :type mins: Numbertype
 :return: 数値を返す。
 :rtype: Numbertype'''
 return val if isinstance(val,(int,float))and 1<=val else mins
def num0s(val:Numbertype=0,mins:Numbertype=0)->Numbertype:
 '''valが0以上の数値かを調べる。

 :param val: 調べたい数値を指定する。
 :type val: Numbertype
 :param mins: 調べたい数値`val`の最低値を指定する。
 :type mins: Numbertype
 :return: 数値を返す。
 :rtype: Numbertype'''
 return val if isinstance(val,(int,float))and 0<=val else mins
def num0(val:Numbertype=0,mins:Numbertype=0)->Numbertype:
 '''valが0より大きい数値かを調べる。

 :param val: 調べたい数値を指定する。
 :type val: Numbertype
 :param mins: 調べたい数値`val`の最低値を指定する。
 :type mins: Numbertype
 :return: 数値を返す。
 :rtype: Numbertype'''
 return val if isinstance(val,(int,float))and 0<val else mins
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
 '''valが0以上の正の整数かを調べる。

 :param val: 調べたい数値を指定する。
 :type val: int
 :param mins: 調べたい数値`val`の最低値を指定する。
 :type mins: int
 :return: 数値を返す。
 :rtype: int'''
 return val if isinstance(val,int)and 0<=val else mins
def int0(val:int=0,mins:int=0)->int:
 '''valが0より大きいの正の整数かを調べる。

 :param val: 調べたい数値を指定する。
 :type val: int
 :param mins: 調べたい数値`val`の最低値を指定する。
 :type mins: int
 :return: 数値を返す。
 :rtype: int'''
 return val if isinstance(val,int)and 0<val else mins
def range_num(
val:Numbertype,
mins:Numbertype=None,
maxs:Numbertype=None,
others:Numbertype=None
)->Numbertype:
 '''valが`mins`から`maxs`の範囲内化を調べる。

 :param val: 範囲内かを調べたい数値を指定する。
 :type val: Numbertype
 :param mins: 範囲の最低値を指定する。
 :type mins: Numbertype
 :param maxs: 範囲の最大値を指定する。
 :type maxs: Numbertype
 :param others: 指定した`val`が指定した範囲ではなかった場合に返す値を指定する。
 :type others: Numbertype
 :return: 数値を返す。
 :rtype: Numbertype'''
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