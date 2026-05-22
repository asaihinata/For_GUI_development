from io import BytesIO
from pathlib import Path,PosixPath,WindowsPath
from typing import IO
from PIL import ImageFile
from PIL._typing import StrOrBytesPath
__all__=['Img_path','Img_byte']
class Img_conversion:
 img:ImageFile
 def __init__(self,data:StrOrBytesPath|IO[bytes]):...
 def get_width(self)->int|float:'''画像データの幅を返す。'''
 def get_height(self)->int|float:'''画像データの高さを返す。'''
 def get_size(self)->tuple[int|float,int|float]:'''画像データのサイズを返す。'''
 def get_format(self)->str|None:'''ソースファイルのファイル形式を返す。'''
 def get_mode(self)->str:'''画像のモードを返す。
 
https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-modes'''
 width=get_width
 height=get_height
 size=get_size
 format=get_format
 mode=get_mode
 def show(self,title:str|None=None):'''画像を表示させる。

 :param title: 画像を表示する際のタイトル名を指定する。
 :type title: str|None'''
class Img_path(Img_conversion):
 path:Path|PosixPath|WindowsPath
 def __init__(self,path:Path|PosixPath|WindowsPath):...
class Img_byte(Img_conversion):
 byte:BytesIO
 def __init__(self,byte:bytes|BytesIO):...