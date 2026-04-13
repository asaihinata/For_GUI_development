from itertools import product
from .._graphhelp import *
class DScatter(threeDElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.x=self._manyarr(kw.get('x'))
  self.y=self._manyarr(kw.get('y'))
  self.z=self._manyarr(kw.get('z'))
  self.label=self.labels(kw.get('label'))[0]
  self.marker=self.markers(kw.get('marker','o'),self.max_depth)
  self.s=num1s(kw.get('markersize'),10)
  self.plot(self.x,self.y,self.z,marker=self.marker,alpha=self.alpha,label=self.label)
 def plot(self,x,y,z,label=None,marker='o',alpha=1):
  self.clear()
  self.graphdata=[self.ax.scatter(xs,ys,zs,label=label[i],marker=marker[i],alpha=alpha)for i,(xs,ys,zs) in enumerate(product(x,y,z))]
  self._apply_labels(self.xlabel,self.ylabel,self.zlabel)
  self.legend()
 def update(self,x=None,y=None,z=None,**kw):
  self._updates(**kw)
  if isinstance(x,NpArraytype):self.x=self._manyarr(x)
  if isinstance(y,NpArraytype):self.y=self._manyarr(y)
  if isinstance(z,NpArraytype):self.z=self._manyarr(z)
  self.marker=self.markers(kw.get('marker',self.marker),self.max_depth)
  self.s=num1s(kw.get('markersize'),self.s)
  self.label=self.labels(kw.get('label',self.label))[0]
  self.plot(self.x,self.y,self.z,marker=self.marker,alpha=self.alpha,label=self.label)
  self._redraw()
 def get(self):return self.graphdata
 def getx(self):return self.x
 def gety(self):return self.y
 def getz(self):return self.z