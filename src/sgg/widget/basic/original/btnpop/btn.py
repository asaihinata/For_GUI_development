from ....dev import listchose,num0,parsecolor
from ...._log import Logger
from ....base import Element
logger=Logger(format={'filename':None,'lineno':{'after':'行目'},'message':None}).get_logger()
__all__=['Btn']
class Btn(Element):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.anchor=listchose(kw.get('anchor'),['center','w','n','s','e','nw','ne','se','sw'])
  self.bg=parsecolor(kw.get('bg'),'#e0e0e0')
  self.wraplength=num0(kw.get('wraplength'))
 def dgettitle(self):return self.title
 def dsettitle(self,titles:str):self.title=titles
 def delta(self):
  try:self.widget.destroy()
  except Exception as e:
   logger.error(e)
 def get_text(self):
  try:
   return self.text
  except Exception as e:
   logger.error(e)
 def set_text(self,txt):
  try:
   self.text=txt
   self.widget.config(text=txt)
  except Exception as e:logger.error(e)
 def get_fg(self):
  try:return str(self.bg)
  except Exception as e:logger.error(e)
 def set_fg(self,fg):
  try:
   self.fg=fg
   self.widget.config(fg=fg)
  except Exception as e:logger.error(e)
 def get_bg(self):
  try:return str(self.bg)
  except Exception as e:logger.error(e)
 def set_bg(self,bg):
  try:
   self.bg=bg
   self.widget.config(bg=bg)
  except Exception as e:
   logger.error(e)