from collections.abc import Iterator
from os import PathLike
from pathlib import Path
from typing import Any
from matplotlib.font_manager import FontEntry,FontProperties
class FontFile:
 Properties:FontProperties
 def __init__(self,path:str|Path|PathLike):'''指定されたフォントファイルのフォントを使用できるようにする。

 :param path: フォントファイルのパスを指定する。
 :type path: str|Path|PathLike
 :raises TypeError: `path`の型がstr,Path,PathLikeではなかった場合に発生させる
 :raises FileNotFoundError: ファイルが見つからなかった場合に発生させる
 :raises ValueError: ファイルの拡張子がafm,otf,ttc,ttfのどれかではなかった場合に発生させる'''
 def __str__(self)->str:...
class Fontmanager:
 '''認識されているフォントについて調べる。'''
 fontmanager:list[FontEntry]
 def __iter__(self)->Iterator[FontEntry]:...
 def __len__(self)->int:...
 def __contains__(self,val:Any)->bool:...
 def __getitem__(self,val:int|slice)->FontEntry|tuple[FontEntry]:...
 def __reversed__(self)->list[FontEntry]:...
 @classmethod
 def fname(cls)->list[str]:'''認識されているフォントのフォントのパスの配列を返す。'''
 @classmethod
 def name(cls)->list[str]:'''認識されているフォントのフォント名の配列を返す。'''
 @classmethod
 def style(cls)->list[str]:'''認識されているフォントのフォントのスタイルの値が入った配列を返す。'''
 @classmethod
 def variant(cls)->list[str]:'''認識されているフォントの`variant`が入った配列を返す。'''
 @classmethod
 def weight(cls)->list[str|int]:'''認識されているフォントの太さの値が入った配列を返す。'''
 @classmethod
 def stretch(cls)->list[str]:'''認識されているフォントの幅の値が入った配列を返す。'''
 @classmethod
 def size(cls)->list[str]:'''認識されているフォントのサイズが入った配列を返す。'''
 def sysfont(self)->list[str]:'''認識されているフォントファイルのパスが入った配列を返す。'''
 @staticmethod
 def sysfont()->list[str]:'''認識されているフォントファイルのパスが入った配列を返す。'''
class Fontentry:
 '''指定されたFontEntryについて調べる'''
 def __init__(self,fontentry:FontEntry)->None:...
 def fname(self)->str:'''`fname`を返す'''
 def name(self)->str:'''`name`を返す'''
 def style(self)->str:'''`style`を返す'''
 def variant(self)->str:'''`variant`を返す'''
 def weight(self)->str|int:'''`weight`を返す'''
 def stretch(self)->str:'''`stretch`を返す'''
 def size(self)->str:'''`size`を返す'''