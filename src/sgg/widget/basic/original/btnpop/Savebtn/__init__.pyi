from ..Btn import *
__all__=['Savebtn']
class Savebtn(Btn):
 def get_path(self)->str:
  '''選択したファイルもしくはフォルダのパスを返す。

 :return: ファイルもしくはフォルダのパスを返す。
 :rtype: str'''