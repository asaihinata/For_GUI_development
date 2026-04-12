from logging import FileHandler
from os.path import abspath,dirname,isfile,join,normpath
from pathlib import Path
from ._clearsave import clearsave
from ._data import log_clear
class LogFile:
 clearj=False
 def __init__(self,file,logger,level,format):
  self.log_file_pas=file if isinstance(file,str) and isfile(Path(file).resolve()) else normpath(join(dirname(abspath(__file__)),'data/log.log'))
  self.c=str(clearsave())
  self._clear_serch()
  file_handler=FileHandler(self.log_file_pas,encoding='utf-8')
  file_handler.setLevel(level)
  file_handler.setFormatter(format)
  logger.addHandler(file_handler)
 def _clear_serch(self):
  for item,key in log_clear.items():
   if self.c in key:
    if item=='do':
     self._log_file_clear()
     break
    elif item=='once' and LogFile.clearj==False:
     self._log_file_clear()
     LogFile.clearj=True
     break
 def _log_file_clear(self):
  with open(self.log_file_pas,'r+')as f:f.truncate(0)