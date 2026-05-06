from logging import FileHandler, Logger


class LogFile:
 def __init__(self,file:str,logger:Logger,level:int,format:str):
  self.log_file_pas=file
  file_handler=FileHandler(self.log_file_pas,encoding='utf-8')
  file_handler.setLevel(level)
  file_handler.setFormatter(format)
  logger.addHandler(file_handler)
 def clear(self):
  with open(self.log_file_pas,'r+')as f:f.truncate(0)