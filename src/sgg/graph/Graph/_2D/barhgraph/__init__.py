from ...dev import *
__all__=['BarhGraph']
class BarhGraph(twoElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.x=NPArray(kw.get('x'),depth_limit=1)
  self.y=NPNumber(kw.get('y'))
  self.logs=bols(kw.get('logs'),False)
  self.height=range_num(num0s(kw.get('height'),1),0,1,1)
  self.align=listchose(kw.get('align'),['center','edge'])
  self.plot(self.x,self.y,label=self.label,alpha=self.alpha,height=self.height,align=self.align,logs=self.logs)
 def plot(self,x,y,label=None,alpha=1,height=1,align='center',logs=False):
  self.clear()
  if y.ndim==1:
   self.graphdata=[self.ax.barh(x,y,label=label[0],alpha=alpha,height=height,align=align,log=logs)]
  else:
   self.graphdata=[self.ax.barh(x,ys,label=label[i],alpha=alpha,height=height,align=align,log=logs)for i,ys in enumerate(y)]
  self._apply_labels(self.xlabel,self.ylabel)
  self.legend()
  self._adjustment()
 def update(self,x=None,y=None,**kw):
  self._updates(**kw)
  if isinstance(x,nListlike):self.x=NPArray(x,depth_limit=1)
  if isinstance(y,nListlike):self.y=NPNumber(y)
  self.height=range_num(num0s(kw.get('height'),self.height),0,1,self.height)
  self.align=listchose(kw.get('align'),['center','edge'],self.align)
  self.logs=bols(kw.get('logs'),self.logs)
  self.plot(self.x,self.y,label=self.label,alpha=self.alpha,height=self.height,align=self.align,logs=self.logs)
  self._redraw()
 def get(self):return self.graphdata
 def getx(self):return self.x
 def gety(self):return self.y