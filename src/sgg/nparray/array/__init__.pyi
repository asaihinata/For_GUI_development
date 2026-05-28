'''簡単な配列の操作をするモジュール'''
__all__=['loop_array']
def loop_array(array:list|tuple,lenght:int)->list|tuple:'''配列の要素を`lenght`回繰り返す。

 :param array: 繰り返したい配列を指定する。
 :type array: list|tuple
 :param lenght: 繰り返す数を指定する。
 :type lenght: int'''