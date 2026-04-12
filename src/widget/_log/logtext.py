from logging import Formatter,LogRecord
from ._data import COLORS,RESET
class TextFormatter(Formatter):
 formats=None
 def format(self,record):
  if not isinstance(record,LogRecord):return record
  self.formats=super().format(record)
  return self.formats
 def __str__(self):return str(self.formats)
class ColorFormatter(Formatter):
 formats=None
 def format(self,record):
  if not isinstance(record,LogRecord):return record
  self.formats=f'{COLORS.get(record.levelno,RESET)}{super().format(record)}{RESET}'
  return self.formats
 def __str__(self):return str(self.formats)