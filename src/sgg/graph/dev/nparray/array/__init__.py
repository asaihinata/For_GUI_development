'''簡単な配列の操作をするモジュール'''
__all__=['loop_array']
def loop_array(array,lenght):
 lens=len(array)
 if lenght<lens:return array[:lenght]
 elif lens<lenght:
  rounding=lenght//lens
  rest=lenght-rounding*lens
  return array*rounding+array[:rest]
 else:return array