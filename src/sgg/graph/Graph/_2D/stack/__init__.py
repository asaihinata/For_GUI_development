from itertools import product
from ...dev import *
__all__=['Stack']
class Stack(twoElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.x=self._onearr(kw.get('x'))
  self.y=self._manyarr(kw.get('y'))
  self.baseline=listchose(kw.get('baseline'),['zero','sym','wiggle','weighted_wiggle'])
  self.hatch=Hatch(kw.get('hatch',None))
  self.plot(self.x,self.y,label=self.label,hatch=self.hatch,baseline=self.baseline,alpha=self.alpha)
 def plot(self,x,y,label=(),hatch=None,baseline='zero',alpha=1):
  self.clear()
  self.graphdata=[self.ax.stackplot(xs,ys,labels=label,hatch=hatch[i],baseline=baseline,alpha=alpha)for i,(xs,ys) in enumerate(product(x,y))]
  self._apply_labels(self.xlabel,self.ylabel)
  self.legend()
  self._adjustment()
 def update(self,x=None,y=None,**kw):
  self._updates(**kw)
  if isinstance(x,nListlike):self.x=self._onearr(x)
  if isinstance(y,nListlike):self.y=self._manyarr(y)
  self.baseline=listchose(kw.get('baseline'),['zero','sym','wiggle','weighted_wiggle'],self.baseline)
  hatch=kw.get('hatch',None)
  self.hatch=parameters(hatch,self.hatch,Hatch(hatch))
  self.plot(self.x,self.y,label=self.label,hatch=self.hatch,baseline=self.baseline)
  self._redraw()
 def get(self):return self.graphdata
 def getx(self):return self.x
 def gety(self):return self.y