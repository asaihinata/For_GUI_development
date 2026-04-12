from json import load
from os.path import dirname,isfile,join
__all__=['getjson']
def getjson(file:str)->dict:
 '''指定されたファイル名のjsonファイルのデータを取得しそれを返す。

 :param file: jsonファイルのファイル名を指定する。
 :type file: str
 :raises FileNotFoundError: `file`で指定したファイル名が存在しなかった場合に発生させる。
 :raises Exception: その他の理由でファイルが読み込まれなかった場合に発生させる。
 :return: jsonのデータを返す。
 :rtype: dict'''
 try:
  jsonpath=join(dirname(__file__),f'{file}.json')
  if not isfile(jsonpath):
   raise FileNotFoundError('ファイルが見つかりません')
  with open(jsonpath,'r',encoding='utf-8')as f:return load(f)
 except Exception as e:
  raise Exception(e)