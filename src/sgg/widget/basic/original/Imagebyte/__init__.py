from tkinter import Label
from PIL import ImageTk
from ...._log import Logger
from ....base import Element
from ...dev import Img_byte
logger=Logger(format={'filename':None,'lineno':{'after':'行目'},'message':None}).get_logger()
__all__=['Imagebyte']
class Imagebyte(Element):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.byte=kw.get('byte')
  self.img=Img_byte(self.byte)
  self.imgs=ImageTk.PhotoImage(image=self.img.imgs.resize(self.img.get_size()))
  self.widget=Label(master,text=None,image=self.imgs,takefocus=self.takefocus)
  self.widget.image=self.imgs
 def delta(self):
  try:self.widget.destroy()
  except Exception as e:
   logger.error(e)