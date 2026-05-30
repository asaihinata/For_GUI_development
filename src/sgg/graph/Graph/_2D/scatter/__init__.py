from itertools import product
from ...dev import *
__all__=['Scatter']
class Scatter(twoElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.x=self._manyarr(kw.get('x'))
  self.y=self._manyarr(kw.get('y'))
  self.marker=Marker(kw.get('marker','o')).marker
  self.s=num1s(kw.get('markersize'),10)
  self.linewidth=num0(kw.get('linewidth'),2)
  self.plot(self.x,self.y,marker=self.marker,linewidth=self.linewidth,alpha=self.alpha,label=self.label,s=self.s)
 def plot(self,x,y,marker='o',linewidth=2,alpha=1,label=None,s=10):
  self.clear()
  self.graphdata=[self.ax.scatter(xs,ys,marker=marker,s=s,alpha=alpha,linewidth=linewidth,label=label[i])for i,(xs,ys) in enumerate(product(x,y))]
  self._apply_labels(self.xlabel,self.ylabel)
  self.legend()
  self._adjustment()
 def update(self,x=None,y=None,**kw):
  self._updates(**kw)
  if isinstance(x,nListlike):self.x=self._manyarr(x)
  if isinstance(y,nListlike):self.y=self._manyarr(y)
  self.marker=Marker(kw.get('marker',self.marker)).marker
  self.s=num1s(kw.get('markersize'),self.s)
  self.alpha=range_num(num0s(kw.get('alpha'),self.alpha),0,1,self.alpha)
  self.linewidth=num0(kw.get('linewidth'),self.linewidth)
  self.plot(self.x,self.y,marker=self.marker,linewidth=self.linewidth,alpha=self.alpha,label=self.label)
  self._redraw()
 def get(self):return self.graphdata
 def getx(self):return self.x
 def gety(self):return self.y