from itertools import product
from .._graphhelp import *
class BarGraph(twoDElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.x=self._onearr(kw.get('x'))
  self.y=self._manyarr(kw.get('y'))
  self.logs=bols(kw.get('logs'),False)
  self.label=self.labels(kw.get('label'))[0]
  self.width=range_num(num0s(kw.get('width'),1),0,1,1)
  self.align=listchose(kw.get('align'),['center','edge'])
  self.plot(self.x,self.y,label=self.label,alpha=self.alpha,width=self.width,align=self.align,logs=self.logs)
 def plot(self,x,y,label=None,alpha=1,width=0.8,align='center',logs=False):
  self.clear()
  for i,(xs,ys) in enumerate(product(x,y)):
   self.graphdata.append(self.ax.bar(xs,ys,log=logs,label=label[i],alpha=alpha,width=width,align=align))
  self._apply_labels(self.xlabel,self.ylabel)
  self.legend()
  self._adjustment()
 def update(self,x=None,y=None,**kw):
  self._updates(**kw)
  if isinstance(x,ndarray|list|tuple):self.x=self._onearr(x)
  if isinstance(y,ndarray|list|tuple):self.y=self._manyarr(y)
  self.width=range_num(num0s(kw.get('width'),self.width),0,1,self.width)
  self.align=listchose(kw.get('align'),['center','edge'],self.align)
  self.logs=bols(kw.get('logs'),self.logs)
  self.plot(self.x,self.y,label=self.label,alpha=self.alpha,width=self.width,align=self.align,logs=self.logs)
  self._redraw()
 def get(self):return self.graphdata
 def getx(self):return self.x
 def gety(self):return self.y
class BarhGraph(twoDElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.x=self._onearr(kw.get('x'))
  self.y=self._manyarr(kw.get('y'))
  self.logs=bols(kw.get('logs'),False)
  self.label=self.labels(kw.get('label'))[0]
  self.height=range_num(num0s(kw.get('height'),1),0,1,1)
  self.align=listchose(kw.get('align'),['center','edge'])
  self.plot(self.x,self.y,label=self.label,alpha=self.alpha,height=self.height,align=self.align,logs=self.logs)
 def plot(self,x,y,label=None,alpha=1,height=1,align='center',logs=False):
  self.clear()
  for i,(xs,ys) in enumerate(product(x,y)):
   self.graphdata.append(self.ax.barh(xs,ys,label=label[i],alpha=alpha,height=height,align=align,log=logs))
  self._apply_labels(self.xlabel,self.ylabel)
  self.legend()
  self._adjustment()
 def update(self,x=None,y=None,**kw):
  self._updates(**kw)
  if isinstance(x,ndarray|list|tuple):self.x=self._onearr(x)
  if isinstance(y,ndarray|list|tuple):self.y=self._manyarr(y)
  self.height=range_num(num0s(kw.get('height'),self.height),0,1,self.height)
  self.align=listchose(kw.get('align'),['center','edge'],self.align)
  self.logs=bols(kw.get('logs'),self.logs)
  self.plot(self.x,self.y,label=self.label,alpha=self.alpha,height=self.height,align=self.align,logs=self.logs)
  self._redraw()
 def get(self):return self.graphdata
 def getx(self):return self.x
 def gety(self):return self.y