from io import BytesIO
from .conversion import Img_conversion
class Img_byte(Img_conversion):
 def __init__(self,byte):
  if not isinstance(byte,bytes):
   raise TypeError('byteにはbytesを指定してください')
  self.byte=BytesIO(byte)
  super().__init__(self.byte)