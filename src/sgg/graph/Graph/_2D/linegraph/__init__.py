from itertools import product
from ...dev import *
__all__=['LineGraph']
class LineGraph(twoElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.x=self._manyarr(kw.get('x'))
  self.y=self._manyarr(kw.get('y'))
  self.marker=Marker(kw.get('marker','none')).marker
  self.markersize=num0(kw.get('markersize'),10)
  self.line=Solid(kw.get('linestyle','-')).solid
  self.linewidth=num0(kw.get('linewidth'),2)
  self.plot(self.x,self.y,marker=self.marker,linewidth=self.linewidth,linestyle=self.line,markersize=self.markersize,alpha=self.alpha,label=self.label)
 def plot(self,x,y,marker='none',linewidth=2,linestyle='-',markersize=10,alpha=1,label=None):
  self.clear()
  self.graphdata=[self.ax.plot(xs,ys,marker=marker,linewidth=linewidth,markersize=markersize,linestyle=linestyle,alpha=alpha,label=label[i])for i,(xs,ys) in enumerate(product(x,y))]
  self._apply_labels(self.xlabel,self.ylabel)
  self.legend()
  self._adjustment()
 def update(self,x=None,y=None,**kw):
  self._updates(**kw)
  if isinstance(x,nListlike):self.x=self._manyarr(x)
  if isinstance(y,nListlike):self.y=self._manyarr(y)
  self.marker=Marker(kw.get('marker',self.marker)).marker
  self.markersize=num0(kw.get('markersize'),self.markersize)
  self.line=self.lines(kw.get('linestyle',self.line),self.max_depth)
  self.linewidth=num0(kw.get('linewidth'),self.linewidth)
  self.plot(self.x,self.y,marker=self.marker,linewidth=self.linewidth,linestyle=self.line,markersize=self.markersize,alpha=self.alpha,label=self.label)
  self._redraw()
 def get(self):return self.graphdata
 def getx(self):return self.x
 def gety(self):return self.y