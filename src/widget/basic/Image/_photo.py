from io import BytesIO
from os.path import basename, isfile, splitext
from pathlib import Path
from urllib.parse import urlparse

from PIL import Image, ImageTk
from requests import get

from ..._function import list2num


class Photo:
 savefile={'bytos':False}
 img=None
 def __init__(self,file=None,size=None):
  self.size=size
  self.file=file
  self.nodofile=file
  try:isfiles=isfile(file)
  except:isfiles=False
  if isinstance(file,bytes):
   self.savefile['bytos']=True
   self.paths=BytesIO(file)
  elif isinstance(file,BytesIO):
   self.savefile['bytos']=True
   self.paths=file
  elif isfiles==True:
   self.paths=Path(file)
   self.savefile['filename']=self.paths.name
   self.savefile['name']=self.paths.stem
   self.savefile['extension']=self.paths.suffix
  elif isfiles==False:
   try:
    basenames=basename(urlparse(file).path)
    self.savefile['filename']=basenames
    (self.savefile['name'],self.savefile['extension'])=splitext(basenames)
    self.paths=BytesIO(get(file).content)
   except:pass
 def data(self):
  try:
   self.img=Image.open(self.paths)
   if list2num(self.size)==False:self.size=self.img.size
   if isinstance(self.size,tuple):self.img=self.img.resize(self.size)
   self.image=ImageTk.PhotoImage(self.img)
  except:self.image=self.file
  return(self.image,self.img,self.savefile)