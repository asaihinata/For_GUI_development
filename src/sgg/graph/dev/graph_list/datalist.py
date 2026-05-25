import numpy as np
class Datalist:
 def __init__(self,data):
  self.data:np.ndarray=data
 def __iter__(self):return iter(self.data)
 def __len__(self):return len(self.data)
 @property
 def ndim(self):return self.data.ndim
 @property
 def shape(self):return self.data.shape
 @property
 def size(self):return self.data.size
 @property
 def T(self):return self.data.T