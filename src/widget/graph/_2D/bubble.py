from itertools import product
from .._graphhelp import *
class Bubble(twoDElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  x,y=self._xys(kw.get('x'),kw.get('y'))
  self.x=self._manyarr(x)
  self.y=self._manyarr(y)
  self.label=self.labels(kw.get('label'))[0]
  self.marker=self.markers(kw.get('marker','o'),self.max_depth)
  self.alpha=range_num(num0s(kw.get('alpha'),0.5),0,1,0.5)
  self.bubblesize=nums(kw.get('bubblesize'),1)
  self.data=self._manyarr(kw.get('data'),False)
  self.datas=self._arr(np.multiply(self.data,self.bubblesize),False)
  self.plot(self.x,self.y,self.datas,marker=self.marker,alpha=self.alpha,label=self.label)
 def plot(self,x,y,data,marker=None,alpha=0.5,label=None):
  self.clear()
  self.graphdata=[self.ax.scatter(xs,ys,marker=marker[i],s=data[i],alpha=alpha,label=label[i])for i,(xs,ys) in enumerate(product(x,y))]
  self.legend()
  self._apply_labels(self.xlabel,self.ylabel)
 def update(self,x=None,y=None,data=None,**kw):
  self._updates(**kw)
  self.bubblesize=nums(kw.get('bubblesize'),self.bubblesize)
  if isinstance(x,NpArraytype):self.x=self._manyarr(x)
  if isinstance(y,NpArraytype):self.y=self._manyarr(y)
  if isinstance(data,NpArraytype):self.data=self._arr(kw.get('data',self.data))
  self.datas=np.multiply(self.data,self.bubblesize)
  self.marker=self.markers(kw.get('marker',self.marker),self.max_depth)
  self.plot(self.x,self.y,marker=self.marker,alpha=self.alpha,label=self.label)
  self._redraw()
 def get(self):return self.graphdata
 def getx(self):return self.x
 def gety(self):return self.y
 def getdata(self):return self.data