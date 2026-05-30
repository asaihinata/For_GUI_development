'''簡単な配列の操作をするモジュール'''
__all__=['loop_array']
def loop_array(array,lenght):
 '''配列の要素を`lenght`回繰り返す。

 :param array: 繰り返したい配列を指定する。
 :type array: list|tuple
 :param lenght: 繰り返す数を指定する。
 :type lenght: int'''
 lens=len(array)
 if lenght<lens:return array[:lenght]
 elif lens<lenght:
  rounding=lenght//lens
  return array*rounding+array[:lenght-rounding*lens]
 else:return array