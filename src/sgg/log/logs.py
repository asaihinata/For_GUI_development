from logging import StreamHandler,getLogger
from os import system as sys
from os.path import dirname,isfile,join,normpath
from pathlib import Path
from platform import system
from ._data import formats_dict
from ._logfile import LogFile
from .logtext import ColorFormatter,TextFormatter
__all__=['Logger']
class Logger:
 log_file_pas=None
 def __init__(self,name='log',level=10,format='message',sep='|',logfile=False,file=None):
  self.sep=sep if isinstance(sep,str) else '|'
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
  if logfile==True:
   if isinstance(file,str) and isfile(Path(file).resolve()):self.log_file_pas=file
   else:self.log_file_pas=normpath(join(dirname(Path(__file__)),'data/log.log'))
   LogFile(self.log_file_pas,self.logger,self.level,TextFormatter(fmt=fotmat,datefmt='%Y-%m-%d %H:%M:%S'))
 def __str__(self):return str(self.formatter)
 def build_format(self,f):
  parts=[]
  if isinstance(f,str):
   if f not in formats_dict:
    raise ValueError('無効なフォーマットキー')
   return formats_dict[f]
  elif isinstance(f,list|tuple):
   for key in f:
    if key not in formats_dict:
     raise ValueError(f'無効なフォーマットキー:{key}')
    parts.append(formats_dict[key])
   return self.sep.join(parts)
  elif isinstance(f,dict):
   led=len(f)-1
   for i,(key,option) in enumerate(f.items()):
    if key not in formats_dict:
     raise ValueError(f'無効なフォーマットキー:{key}')
    base=formats_dict[key]
    settxt=base if option==None else f'{option.get('before')}{base}{option.get('after',self.sep)}'
    if led!=i:settxt=settxt+self.sep
    parts.append(settxt)
   return ''.join(parts)
  raise TypeError('フォーマットは文字型か配列型,辞書型で指定してください')
 def get_logger(self):return self.logger
 def get_logfilepath(self):return self.log_file_pas
 def read_log(self):
  if self.log_file_pas is None:
   raise FileNotFoundError('ログファイルが存在しません')
  with open(self.log_file_pas,'r')as f:return f.read()
 @staticmethod
 def clear():sys('cls' if system()=='Windows'else'clear')