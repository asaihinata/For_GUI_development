from io import BytesIO
from pathlib import Path,PosixPath,WindowsPath
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