from json import load
from os.path import dirname,isfile,join
__all__=['getjson']
def getjson(file:str)->dict:
 '''指定されたファイル名のjsonファイルのデータを取得しそれを返す。

 :param file: jsonファイルのファイル名を指定する。
 :type file: str
 :raises FileNotFoundError: `file`で指定したファイル名が存在しなかった場合に発生させる。
 :return: jsonのデータを返す。
 :rtype: dict'''
 jsonpath=join(dirname(__file__),f'{file}.json')
 if not isfile(jsonpath):
  raise FileNotFoundError('指定されたファイルが見つかりません')
 with open(jsonpath,'r',encoding='utf-8')as f:return load(f)