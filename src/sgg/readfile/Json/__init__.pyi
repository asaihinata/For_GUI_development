'''jsonファイルのデータを取得するモジュール'''
from pathlib import Path
from typing import Any
__all__=['Getjosn']
class Getjosn:
 def __init__(
self,
path:Path|str
)->None:'''jsonファイルのデータを取得する。

 :param path: jsonファイルのパスを指定する。
 :type path: Path|str
 :raises ValueError: `path`で指定されたパスがjsonファイルではない時に発生させる'''
 @property
 def json(self)->Any:'''jsonファイルのデータを取得する。

 :return: jsonファイルのデータを返す。
 :rtype: Any'''
 def get_json(self)->Any:'''jsonファイルのデータを取得する。

 :return: jsonファイルのデータを返す。
 :rtype: Any'''