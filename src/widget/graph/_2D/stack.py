from itertools import product
from .._graphhelp import *
class Stack(twoDElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.x=self._onearr(kw.get('x'))
  self.y=self._manyarr(kw.get('y'))
  self.label=self.labels(kw.get('label'))[0]
  self.baseline=listchose(kw.get('baseline'),['zero','sym','wiggle','weighted_wiggle'])
  self.hatch=self._list_loop(list(Hatch(kw.get('hatch'))),self.max_depth)
  self.plot(self.x,self.y,label=self.label,hatch=self.hatch,baseline=self.baseline,alpha=self.alpha)
 def plot(self,x,y,label=None,hatch=None,baseline='zero',alpha=1):
  self.clear()
  self.graphdata=[self.ax.stackplot(xs,ys,labels=label[i],hatch=hatch[i],baseline=baseline,alpha=alpha)for i,(xs,ys) in enumerate(product(x,y))]
  self._apply_labels(self.xlabel,self.ylabel)
  self.legend()
  self._adjustment()
 def update(self,x=None,y=None,**kw):
  self._updates(**kw)
  if isinstance(x,np.ndarray|list|tuple):self.x=self._onearr(x)
  if isinstance(y,np.ndarray|list|tuple):self.y=self._manyarr(y)
  self.label=self.labels(kw.get('label',self.label))[0]
  self.baseline=listchose(kw.get('baseline'),['zero','sym','wiggle','weighted_wiggle'],self.baseline)
  self.hatch=self._list_loop(list(Hatch(kw.get('hatch',self.hatch))),self.max_depth)
  self.plot(self.x,self.y,label=self.label,hatch=self.hatch,baseline=self.baseline)
  self._redraw()
 def get(self):return self.graphdata
 def getx(self):return self.x
 def gety(self):return self.y