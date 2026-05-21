from PIL import Image
__all__=['Img_conversion']
class Img_conversion:
 def __init__(self,data):
  self.imgs=Image.open(data)
 def get_width(self):return self.imgs.width
 def get_height(self):return self.imgs.height
 def get_size(self):return self.imgs.width,self.imgs.height
 def get_format(self):return self.imgs.format
 def get_mode(self):return self.imgs.mode
 def show(self):self.imgs.show()