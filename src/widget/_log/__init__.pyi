import logging
from typing import NoReturn
class Logger:
 def __init__(
self,
name:str='log',
level:int=10,
format:str|tuple[str,...]|dict='message',
sep:str='|',
logfile:bool=False,
file:str=...
)->None:'''ログを作成する。

 :param name: ログ名を指定する。
 :type name: str
 :param level: ログレベルを指定する。
 :type level: int
 :param format: ログで表示するテキストを指定する。
 :type format: str|tuple[str,...]|dict
 :param sep: formatで複数項目を指定した際の区切り文字を指定する。sepを文字型以外で指定した場合`|`を返す。
 :type sep: str
 :param logfile: ログファイルにログを保存するか指定する。
 :type logfile: bool
 :param file: ログの保存先のファイルを指定する。
 :type file: str'''
 def get_logger(self)->logging.Logger:'''logging.Loggerを返す。

 :return: `logging.Logger`を返す。
 :rtype: logging.Logger'''
 def read_log(self)->str:'''ログファイルのログを読み取る。

 :raises FileNotFoundError: ログファイルが存在しない場合に発生させる。
 :return: ログファイルのログを返す。
 :rtype: str'''
 def get_logfilepath(self)->str|None:'''ログファイルのファイルパスを返す。'''
 @classmethod
 def clear(cls)->NoReturn:'''コンソールを消す。'''
 def __str__(self)->str:...