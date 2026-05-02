from os import PathLike
from pathlib import Path
from matplotlib.font_manager import FontProperties
__all__=['FontFile']
class FontFile:
 def __init__(self,path):
  if not isinstance(path,(str,Path,PathLike)):
   raise TypeError('pathの型が違います')
  self.path=Path(path)
  if not self.path.exists():
   raise FileNotFoundError('パスが存在していません')
  if not self.path.suffix in ['.afm','.otf','.ttc','.ttf']:
   raise ValueError('ファイルの拡張子がafm,otf,ttc,ttfのどれかではありません')
  self.Properties=FontProperties(fname=path)
 def __str__(self):return str(self.path)
 def __fspath__(self):return self.path