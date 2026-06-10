from io import BytesIO
from pathlib import Path, PosixPath, WindowsPath

from PIL import Image

__all__=['Img_path','Img_byte']
class Img_conversion:
 def __init__(self,data):
  self.imgs=Image.open(data)
 def get_width(self):return self.imgs.width
 def get_height(self):return self.imgs.height
 def get_size(self):return self.imgs.width,self.imgs.height
 def get_format(self):return self.imgs.format
 def get_mode(self):return self.imgs.mode
 width=get_width
 height=get_height
 size=get_size
 format=get_format
 mode=get_mode
 def show(self,title=None):self.imgs.show(title)
 def resize(self,w,h):
  if not isinstance(w,int):
   raise TypeError('wには整数型を指定してください')
  elif w<=1:
   raise ValueError('wには1以上の整数を指定してください')
  if not isinstance(h,int):
   raise TypeError('hには整数型を指定してください')
  elif h<=1:
   raise ValueError('hには1以上の整数を指定してください')
  self.imgs.resize((w,h))
  return self
 def asresize(self):
  self.imgs.resize(self.get_size())
  return self
class Img_path(Img_conversion):
 def __init__(self,path):
  if not isinstance(path,Path|PosixPath|WindowsPath):
   raise TypeError('pathにはpathlib.Pathを指定してください')
  self.path=path
  super().__init__(self.path)
class Img_byte(Img_conversion):
 def __init__(self,byte):
  if not isinstance(byte,bytes|BytesIO):
   raise TypeError('byteにはbytesもしくはBytesIOの型で指定してください')
  if isinstance(byte,bytes):self.byte=BytesIO(byte)
  else:self.byte=byte
  super().__init__(self.byte)