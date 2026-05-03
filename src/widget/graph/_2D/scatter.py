from itertools import product
from .._graphhelp import *
class Scatter(twoDElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.x=self._manyarr(kw.get('x'))
  self.y=self._manyarr(kw.get('y'))
  self.label=self.labels(kw.get('label'))[0]
  self.marker=self.markers(kw.get('marker','o'),self.max_depth)
  self.s=num1s(kw.get('markersize'),10)
  self.linewidth=num0(kw.get('linewidth'),2)
  self.plot(self.x,self.y,marker=self.marker,linewidth=self.linewidth,alpha=self.alpha,label=self.label,s=self.s)
 def plot(self,x,y,marker=None,linewidth=2,alpha=1,label=None,s=10):
  self.clear()
  self.graphdata=[self.ax.scatter(xs,ys,marker=marker[i],s=s,alpha=alpha,linewidth=linewidth,label=label[i])for i,(xs,ys) in enumerate(product(x,y))]
  self._apply_labels(self.xlabel,self.ylabel)
  self.legend()
  self._adjustment()
 def update(self,x=None,y=None,**kw):
  self._updates(**kw)
  if isinstance(x,ndarray|list|tuple):self.x=self._manyarr(x)
  if isinstance(y,ndarray|list|tuple):self.y=self._manyarr(y)
  self.marker=self.markers(kw.get('marker',self.marker),self.max_depth)
  self.s=num1s(kw.get('markersize'),self.s)
  self.alpha=range_num(num0s(kw.get('alpha'),self.alpha),0,1,self.alpha)
  self.linewidth=num0(kw.get('linewidth'),self.linewidth)
  self.plot(self.x,self.y,marker=self.marker,linewidth=self.linewidth,alpha=self.alpha,label=self.label)
  self._redraw()
 def get(self):return self.graphdata
 def getx(self):return self.x
 def gety(self):return self.y