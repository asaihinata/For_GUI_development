import logging
from ...types import Literal,NoReturn
class Logger:
 def __init__(
self,
name:str='log',
level:int=10,
format:str|list='message',
sep:str='|',
logfile:bool=False,
file:str=...,
lclear:Literal['none','once','do',None,'',' ']='none'
)->None:'''ログを作成する。

 :param name: ログ名を指定する。
 :type name: str
 :param level: ログレベルを指定する。
 :type level: int
 :param format: ログで表示するテキストを指定する。
 :type format: str|list
 :param sep: formatで複数項目を指定した際の区切り文字を指定する。sepを文字型以外で指定した場合'|'を返す。
 :type sep: str
 :param logfile: ログファイルにログを保存するか指定する。
 :type logfile: bool
 :param file: ログの保存先のファイルを指定する。
 :type file: str
 :param lclear: ログファイルに書き込まれたログの削除の仕方を指定する。
 :type lclear: Literal['none','once','do',None,'',' ']'''
 def get_logger(self)->logging.Logger:'''logging.Loggerを返す。

 :return: self.logger
 :rtype: logging.Loggerを返す。'''
 @classmethod
 def clear(cls)->NoReturn:'''コンソールを消す。'''