from pathlib import Path,WindowsPath
from .conversion import Img_conversion
class Img_path(Img_conversion):
 def __init__(self,path):
  if not isinstance(path,Path|WindowsPath):
   raise TypeError('pathにはpathlib.Pathを指定してください')
  self.path=path
  super().__init__(self.path)