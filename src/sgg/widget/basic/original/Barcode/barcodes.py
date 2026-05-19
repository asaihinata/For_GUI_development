from io import BytesIO
from barcode import get_class
from barcode.writer import ImageWriter
__all__=['barcode_data']
support_barcode=['codabar','code128','code39','ean','ean13','ean13-guard','ean14','ean8','ean8-guard','gs1','gs1_128','gtin','isbn','isbn10','isbn13','issn','itf','jan','nw-7','pzn','upc','upca']
class barcode_data:
 byte_buffer=BytesIO()
 def __init__(self,value,format='code39'):
  self.format=format if format in support_barcode else 'code39'
  self.classbarcode=get_class(self.format)
  self.barcodes=self.classbarcode(value,writer=ImageWriter())
  self.barcodes.write(self.byte_buffer)
  self.byte_buffer.seek(0)
  self.bytedata=self.byte_buffer.read()
 def get_type(self):return self.classbarcode.name