from logging import StreamHandler,getLogger
from os import system as sys
from platform import system
from ._clearsave import clearsave
from ._data import formats_dict
from ._logfile import LogFile
from .logtext import ColorFormatter,TextFormatter
__all__=['Logger']
class Logger:
 def __init__(self,name='log',level=10,format='message',sep='|',logfile=False,file=None,lclear='none'):
  self.sep=sep if isinstance(sep,str) else '|'
  clearsave(lclear)
  self.level=level
  self.logger=getLogger(name)
  self.logger.setLevel(level)
  self.logger.propagate=False
  if self.logger.hasHandlers():self.logger.handlers.clear()
  fotmat=self.build_format(format)
  self.formatter=ColorFormatter(fmt=fotmat,datefmt='%Y-%m-%d %H:%M:%S')
  self.handler=StreamHandler()
  self.handler.setLevel(level)
  self.handler.setFormatter(self.formatter)
  self.logger.addHandler(self.handler)
  self.logfile=logfile if isinstance(logfile,bool) else False
  if self.logfile:LogFile(file=file,logger=self.logger,level=self.level,format=TextFormatter(fmt=fotmat,datefmt='%Y-%m-%d %H:%M:%S'))
 def __str__(self):return str(self.formatter)
 def build_format(self,f):
  parts=[]
  if isinstance(f,str):
   if f not in formats_dict:
    raise ValueError('invalid format key')
   return formats_dict[f]
  elif isinstance(f,list):
   for key in f:
    if key not in formats_dict:
     raise ValueError(f'invalid format key:{key}')
    parts.append(formats_dict[key])
   return self.sep.join(parts)
  elif isinstance(f,dict):
   led=len(f)-1
   for i,(key,option) in enumerate(f.items()):
    if key not in formats_dict:
     raise ValueError(f'invalid format key:{key}')
    base=formats_dict[key]
    settxt=base if option==None else f'{option.get('before')}{base}{option.get('after',self.sep)}'
    if led!=i:settxt=settxt+self.sep
    parts.append(settxt)
   return ''.join(parts)
  raise TypeError('format must be str,list,or dict')
 def get_logger(self):return self.logger
 @staticmethod
 def clear():sys('cls' if system()=='Windows'else'clear')